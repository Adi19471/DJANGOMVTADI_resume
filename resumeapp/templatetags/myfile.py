from django import template
register = template.Library()


@register.filter(name = 'remove_special')
def remove_cahr(value,arg):
    print("ARG:",arg)
    print("VALUE:",value)
    for character in arg:
        value = value.replace(character, "")
    return value
