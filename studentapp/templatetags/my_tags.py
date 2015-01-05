# -*- coding: utf-8 -*-

import re

from django.conf import settings
from django import template
from django.template.base import (Node, NodeList)
from django.utils.safestring import mark_safe
from django.utils.encoding import force_text

register = template.Library()


def _render_nodelist_items(nodelist, context, result=None):
    if result is None:
        result = []
    for node in nodelist:
        if not isinstance(node, template.Node):
            result.append(node)
        else:
            try:
                result.append(nodelist.render_node(node, context))
            except Exception, ex:
                # get the wrapped exception if settings.DEBUG is True
                if hasattr(ex, 'exc_info'):
                    ex = ex.exc_info[1]
                # let every exception other than StopLoopException propagate
                if not isinstance(ex, StopLoopException):
                    raise
                # reraise the StopLoopException with the updated nodelist
                if ex.nodelist:
                    result.extend(ex.nodelist)
                ex.nodelist = result
                raise ex
    return result

class StopLoopException(Exception):
    def __init__(self, loop, continue_, nodelist=None):
        if not isinstance(loop, Loop):
            raise TypeError('Loop instance expected, %s given' % loop.__class__.__name__)
        super(StopLoopException, self).__init__(loop, continue_, nodelist)
        self.loop, self.continue_, self.nodelist = self.args

class Loop(dict):
    '''Base class of loop variables passed in the context (e.g. 'forloop').
    A loop instance holds and keeps up to date the attributes exposed in the
    context. This class exposes ``counter``, ``counter0``, ``first`` and
    ``parentloop``; its :class:`BoundedLoop` subclass adds ``revcounter``,
    ``revcounter0`` and ``last``.
    Additionally, a loop instance renders the items of the nodelist that comprise
    the loop and accumulates the rendered strings on every call to :meth:`next`.
    :meth:`next` also handles continuing or breaking from the loop and informs
    the caller accordingly.
    '''

    PASS = object()
    BREAK = object()
    CONTINUE = object()

    def __init__(self, name, context, nodelist):
        self._name = name
        self._context = context
        self._nodelist = nodelist
        self._rendered_nodelist = template.NodeList()
        self['parentloop'] = context.get(name)
        context.push()
        context[name] = self

    def render(self, close=False):
        '''Renders the accumulated nodelist for this loop.
        As a convenience, if ``close`` is true, the loop is also :meth:`close`d.
        '''
        if close:
            self.close()
        return self._rendered_nodelist.render(self._context)
    render.alters_data = True

    def next(self):
        '''Updates this loop for one iteration step.
        :returns: The status of the loop after this step: :attr:`CONTINUE` if a
            ``continue`` targeting this loop was encountered, :attr:`BREAK` for
            a break, or :attr:`PASS` otherwise.
        :raises StopLoopException: If a ``break`` or ``continue`` for a loop
            other than this one (presumably an ancestor) was encountered.
        '''
        if self._nodelist is None:
            raise RuntimeError('This loop is inactive')
        try: # update the exposed attributes
            counter = self['counter']
            self.update(counter0=counter, counter=counter+1, first=False)
        except KeyError:
            # initialize the exposed attributes the first time this is called
            self.update(counter0=0, counter=1, first=True)
        try:
            _render_nodelist_items(self._nodelist, self._context, self._rendered_nodelist)
            status = self.PASS
        except StopLoopException, ex:
            # if this is not the target loop, keep bubbling up the exception
            if ex.loop is not self:
                raise
            # pop context until (but excluding) the dict that contains this loop
            self._pop_context_until_self(inclusive=False)
            status = ex.continue_ and self.CONTINUE or self.BREAK
        return status
    next.alters_data = True

    def close(self):
        '''Mark this loop as closed.
        After a loop is closed, subsequent calls to :meth:`next` are not allowed.
        This should be called when the loop is "done" to remove any loop-specific
        context entries.
        '''
        if self._nodelist:
            self._pop_context_until_self(inclusive=True)
            self._nodelist = None
    close.alters_data = True

    def _pop_context_until_self(self, inclusive):
        name = self._name
        dicts = self._context.dicts
        while len(dicts) > 1:
            if dicts[-1].get(name) is self:
                if inclusive:
                    del dicts[-1]
                break
            del dicts[-1]

@register.tag('while')
class WhileNode(template.Node):
    '''Loops over a block as long as a boolean expression is "true".

    For example, to pop each athlete from a list of athletes ``athlete_list``::

        <ul>
        {% while athlete_list %}
            <li>{{ athlete_list.pop.name }}</li>
        {% endwhile %}
        </ul>

    The while loop sets a number of variables available within the loop:

        ==========================  ================================================
        Variable                    Description
        ==========================  ================================================
        ``whileloop.counter``       The current iteration of the loop (1-indexed)
        ``whileloop.counter0``      The current iteration of the loop (0-indexed)
                                    loop (0-indexed)
        ``whileloop.first``         True if this is the first time through the loop
        ``whileloop.parentloop``    For nested loops, this is the loop "above" the
                                    current one
        ==========================  ================================================

    You can also ``continue`` or ``break`` from the loop by using the respective
    filters on the ``whileloop`` variable::

        <ul>
        {% while athlete_list %}
            {% with athlete_list.pop.name as athlete %}
                {% if athlete == 'Woods' %}
                    {{ whileloop|continue }}
                {% endif %}
                <li>{{ athlete }}</li>
                {% if athlete == 'Pele' %}
                    {{ whileloop|break }}
                {% endif %}
            {% endwith %}
        {% endwhile %}
        </ul>
    '''

    child_nodelists = ('nodelist_loop',)

    def __init__(self, parser, token):
        bits = token.split_contents()[1:]
        self.var = template.defaulttags.TemplateIfParser(parser, bits).parse()
        self.nodelist_loop = parser.parse(('endwhile',))
        parser.delete_first_token()

    def __rer__(self):
        return "<While node>"

    def __iter__(self):
        return self.nodelist_loop

    def render(self, context):
        loop = Loop('whileloop', context, self.nodelist_loop)
        eval_var = self.var.eval
        while True:
            try:
                if not eval_var(context):
                    break
            except template.VariableDoesNotExist:
                break
            if loop.next() is loop.BREAK:
                break
        return loop.render(close=True)



# class WhileNode(Node):
#     child_nodelists = ('nodelist_loop', 'nodelist_empty')

#     def __init__(self, loopvars, sequence, is_reversed, nodelist_loop, nodelist_empty=None):
#         self.loopvars, self.sequence = loopvars, sequence
#         self.is_reversed = is_reversed
#         self.nodelist_loop = nodelist_loop
#         if nodelist_empty is None:
#             self.nodelist_empty = NodeList()
#         else:
#             self.nodelist_empty = nodelist_empty

#     def __repr__(self):
#         reversed_text = ' reversed' if self.is_reversed else ''
#         return "<For Node: for %s in %s, tail_len: %d%s>" % \
#             (', '.join(self.loopvars), self.sequence, len(self.nodelist_loop),
#              reversed_text)

#     def __iter__(self):
#         for node in self.nodelist_loop:
#             yield node
#         for node in self.nodelist_empty:
#             yield node

#     def render(self, context):
#         if 'forloop' in context:
#             parentloop = context['forloop']
#         else:
#             parentloop = {}
#         with context.push():
#             try:
#                 values = self.sequence.resolve(context, True)
#             except VariableDoesNotExist:
#                 values = []
#             if values is None:
#                 values = []
#             if not hasattr(values, '__len__'):
#                 values = list(values)
#             len_values = len(values)
#             if len_values < 1:
#                 return self.nodelist_empty.render(context)
#             nodelist = []
#             if self.is_reversed:
#                 values = reversed(values)
#             unpack = len(self.loopvars) > 1
#             # Create a forloop value in the context.  We'll update counters on each
#             # iteration just below.
#             loop_dict = context['forloop'] = {'parentloop': parentloop}
#             for i, item in enumerate(values):
#                 # Shortcuts for current loop iteration number.
#                 loop_dict['counter0'] = i
#                 loop_dict['counter'] = i + 1
#                 # Reverse counter iteration numbers.
#                 loop_dict['revcounter'] = len_values - i
#                 loop_dict['revcounter0'] = len_values - i - 1
#                 # Boolean values designating first and last times through loop.
#                 loop_dict['first'] = (i == 0)
#                 loop_dict['last'] = (i == len_values - 1)

#                 pop_context = False
#                 if unpack:
#                     # If there are multiple loop variables, unpack the item into
#                     # them.
#                     try:
#                         unpacked_vars = dict(zip(self.loopvars, item))
#                     except TypeError:
#                         pass
#                     else:
#                         pop_context = True
#                         context.update(unpacked_vars)
#                 else:
#                     context[self.loopvars[0]] = item
#                 # In TEMPLATE_DEBUG mode provide source of the node which
#                 # actually raised the exception
#                 if settings.TEMPLATE_DEBUG:
#                     for node in self.nodelist_loop:
#                         try:
#                             nodelist.append(node.render(context))
#                         except Exception as e:
#                             if not hasattr(e, 'django_template_source'):
#                                 e.django_template_source = node.source
#                             raise
#                 else:
#                     for node in self.nodelist_loop:
#                         nodelist.append(node.render(context))
#                 if pop_context:
#                     # The loop variables were pushed on to the context so pop them
#                     # off again. This is necessary because the tag lets the length
#                     # of loopvars differ to the length of each set of items and we
#                     # don't want to leave any vars from the previous loop on the
#                     # context.
#                     context.pop()
#         return mark_safe(''.join(force_text(n) for n in nodelist))


# @register.tag('while')
# def do_while(parser, token):
#     bits = token.split_contents()
#     if len(bits) < 4:
#         raise TemplateSyntaxError("'while' statements should have at least four"
#                                   " words: %s" % token.contents)

#     is_reversed = bits[-1] == 'reversed'
#     in_index = -3 if is_reversed else -2
#     if bits[in_index] != 'in':
#         raise TemplateSyntaxError("'while' statements should use the format"
#                                   " 'while x in y': %s" % token.contents)

#     loopvars = re.split(r' *, *', ' '.join(bits[1:in_index]))
#     for var in loopvars:
#         if not var or ' ' in var:
#             raise TemplateSyntaxError("'while' tag received an invalid argument:"
#                                       " %s" % token.contents)

#     sequence = parser.compile_filter(bits[in_index + 1])
#     nodelist_loop = parser.parse(('empty', 'endwhile',))
#     token = parser.next_token()
#     if token.contents == 'empty':
#         nodelist_empty = parser.parse(('endwhile',))
#         parser.delete_first_token()
#     else:
#         nodelist_empty = None
#     return WhileNode(loopvars, sequence, is_reversed, nodelist_loop, nodelist_empty)