from django import template

register = template.Library()

@register.filter(name='get_range')
def get_range(value, max_value):
    return range(value, max_value + 1)

