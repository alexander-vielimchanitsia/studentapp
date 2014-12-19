from django import template

register = template.Library()


@register.filter()
def str2int(val, arg):
    try:
        return int(val) + int(arg)
    except (TypeError, ValueError):
        try:
            return val + arg
        except Exception:
            return ''