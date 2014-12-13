from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(name='add_class')
def add_class(field, css):
    return field.as_widget(attrs={"class": css})


@register.filter(name='att')
def add_attr(field, attr):
    attribute = attr.split(';')
    attrs = {}
    for string in attribute:
        kv = string.split(':')
        attrs[kv[0]] = kv[1]
    return field.as_widget(attrs=attrs)


@register.filter(name='get_error')
def get_error(dict, key):
    error_message = ""
    if key in dict:
        errors = dict[key]
        for error in errors:
            error_message += error
    return error_message