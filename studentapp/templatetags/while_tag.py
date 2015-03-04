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


# MinusOne - віднімає одиничку від змінної і зберігає нові дані в шаблоні
class MinusOneNode(template.Node):
    def __init__(self, format_string):
        self.format_string = template.Variable(format_string)

    def render(self, context):
        var = self.format_string.resolve(context)

        try:
            result = int(var) - int(1)
        except (TypeError, ValueError):
            try:
                result = var - 1
            except Exception:
                result = 0

        context[self.format_string.var] = result

        return ''



@register.tag
def minusone(parser,token):
    try:
        # split_contents() knows not to split quoted strings.
        tag_name, format_string = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError("%r tag requires a single argument" % token.contents.split()[0])
    return MinusOneNode(format_string)