from django import template

register = template.Library()


@register.filter(name='str2int')
def str2int(value):
    if value = str():
        value_int = eval(value)
    return value