from re import escape
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.inclusion_tag('home/partials/navbar-html.html')
def topbar(user):
    print(user)
    return {'username': user }

@register.inclusion_tag('home/partials/breadcrumbs.html')
def breadcrumb(list):
    return {'breadcrumb': list }

@register.filter(name='truncate_and_escape')
def truncate_and_escape(text, max_words):
    words = text.split(' ')
    if len(words) > max_words:
        truncated_text = ' '.join(words[:max_words]) + '...'
    else:
        truncated_text = ' '.join(words)

    truncated_text = truncated_text.lstrip('<p>').rstrip('</p>')
    
    return mark_safe(truncated_text)

@register.filter(name='lowercase')
def lower(value):
    """Converts a string into all lowercase"""
    return value.lower()