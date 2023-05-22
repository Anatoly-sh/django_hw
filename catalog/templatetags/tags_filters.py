from django import template


register = template.Library()


@register.filter
def media_path(path):
    return '/media/' + str(path)


@register.simple_tag
def media_path(path):
    return '/media/' + str(path)
