import re

from django.conf import settings
from django import template
from django.template.base import (Node, NodeList)
from django.utils.safestring import mark_safe
from django.utils.encoding import force_text

register = template.Library()


class ForNode(Node):
    child_nodelists = ('nodelist_loop', 'nodelist_empty')

    def __init__(self, loopvars, sequence, is_reversed, nodelist_loop, nodelist_empty=None):
        self.loopvars, self.sequence = loopvars, sequence
        self.is_reversed = is_reversed
        self.nodelist_loop = nodelist_loop
        if nodelist_empty is None:
            self.nodelist_empty = NodeList()
        else:
            self.nodelist_empty = nodelist_empty

    def __repr__(self):
        reversed_text = ' reversed' if self.is_reversed else ''
        return "<For Node: for %s in %s, tail_len: %d%s>" % \
            (', '.join(self.loopvars), self.sequence, len(self.nodelist_loop),
             reversed_text)

    def __iter__(self):
        for node in self.nodelist_loop:
            yield node
        for node in self.nodelist_empty:
            yield node

    def render(self, context):
        if 'forloop' in context:
            parentloop = context['forloop']
        else:
            parentloop = {}
        with context.push():
            try:
                values = self.sequence.resolve(context, True)
            except VariableDoesNotExist:
                values = []
            if values is None:
                values = []
            if not hasattr(values, '__len__'):
                values = list(values)
            len_values = len(values)
            if len_values < 1:
                return self.nodelist_empty.render(context)
            nodelist = []
            if self.is_reversed:
                values = reversed(values)
            unpack = len(self.loopvars) > 1
            # Create a forloop value in the context.  We'll update counters on each
            # iteration just below.
            loop_dict = context['forloop'] = {'parentloop': parentloop}
            for i, item in enumerate(values):
                # Shortcuts for current loop iteration number.
                loop_dict['counter0'] = i
                loop_dict['counter'] = i + 1
                # Reverse counter iteration numbers.
                loop_dict['revcounter'] = len_values - i
                loop_dict['revcounter0'] = len_values - i - 1
                # Boolean values designating first and last times through loop.
                loop_dict['first'] = (i == 0)
                loop_dict['last'] = (i == len_values - 1)

                pop_context = False
                if unpack:
                    # If there are multiple loop variables, unpack the item into
                    # them.
                    try:
                        unpacked_vars = dict(zip(self.loopvars, item))
                    except TypeError:
                        pass
                    else:
                        pop_context = True
                        context.update(unpacked_vars)
                else:
                    context[self.loopvars[0]] = item
                # In TEMPLATE_DEBUG mode provide source of the node which
                # actually raised the exception
                if settings.TEMPLATE_DEBUG:
                    for node in self.nodelist_loop:
                        try:
                            nodelist.append(node.render(context))
                        except Exception as e:
                            if not hasattr(e, 'django_template_source'):
                                e.django_template_source = node.source
                            raise
                else:
                    for node in self.nodelist_loop:
                        nodelist.append(node.render(context))
                if pop_context:
                    # The loop variables were pushed on to the context so pop them
                    # off again. This is necessary because the tag lets the length
                    # of loopvars differ to the length of each set of items and we
                    # don't want to leave any vars from the previous loop on the
                    # context.
                    context.pop()
        return mark_safe(''.join(force_text(n) for n in nodelist))


@register.tag('while')
def do_while(parser, token):
    """
    Loops over each item in an array.

    For example, to display a list of athletes given ``athlete_list``::

        <ul>
        {% for athlete in athlete_list %}
            <li>{{ athlete.name }}</li>
        {% endfor %}
        </ul>

    You can loop over a list in reverse by using
    ``{% for obj in list reversed %}``.

    You can also unpack multiple values from a two-dimensional array::

        {% for key,value in dict.items %}
            {{ key }}: {{ value }}
        {% endfor %}

    The ``for`` tag can take an optional ``{% empty %}`` clause that will
    be displayed if the given array is empty or could not be found::

        <ul>
          {% for athlete in athlete_list %}
            <li>{{ athlete.name }}</li>
          {% empty %}
            <li>Sorry, no athletes in this list.</li>
          {% endfor %}
        <ul>

    The above is equivalent to -- but shorter, cleaner, and possibly faster
    than -- the following::

        <ul>
          {% if althete_list %}
            {% for athlete in athlete_list %}
              <li>{{ athlete.name }}</li>
            {% endfor %}
          {% else %}
            <li>Sorry, no athletes in this list.</li>
          {% endif %}
        </ul>

    The for loop sets a number of variables available within the loop:

        ==========================  ================================================
        Variable                    Description
        ==========================  ================================================
        ``forloop.counter``         The current iteration of the loop (1-indexed)
        ``forloop.counter0``        The current iteration of the loop (0-indexed)
        ``forloop.revcounter``      The number of iterations from the end of the
                                    loop (1-indexed)
        ``forloop.revcounter0``     The number of iterations from the end of the
                                    loop (0-indexed)
        ``forloop.first``           True if this is the first time through the loop
        ``forloop.last``            True if this is the last time through the loop
        ``forloop.parentloop``      For nested loops, this is the loop "above" the
                                    current one
        ==========================  ================================================

    """
    bits = token.split_contents()
    if len(bits) < 4:
        raise TemplateSyntaxError("'while' statements should have at least four"
                                  " words: %s" % token.contents)

    is_reversed = bits[-1] == 'reversed'
    in_index = -3 if is_reversed else -2
    if bits[in_index] != 'in':
        raise TemplateSyntaxError("'while' statements should use the format"
                                  " 'while x in y': %s" % token.contents)

    loopvars = re.split(r' *, *', ' '.join(bits[1:in_index]))
    for var in loopvars:
        if not var or ' ' in var:
            raise TemplateSyntaxError("'while' tag received an invalid argument:"
                                      " %s" % token.contents)

    sequence = parser.compile_filter(bits[in_index + 1])
    nodelist_loop = parser.parse(('empty', 'endwhile',))
    token = parser.next_token()
    if token.contents == 'empty':
        nodelist_empty = parser.parse(('endwhile',))
        parser.delete_first_token()
    else:
        nodelist_empty = None
    return ForNode(loopvars, sequence, is_reversed, nodelist_loop, nodelist_empty)