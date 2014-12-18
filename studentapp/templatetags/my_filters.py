from django import template


register = template.Library()


@register.filter()
def str2int(value, arg):
    try:
        return int(value) + int(arg)
    except (ValueError, TypeError):
        try:
            return value + arg
        except Exception:
            return ''