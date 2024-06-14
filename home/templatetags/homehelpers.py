from re import escape
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(name='limit_words')
def limit_words(value, arg):
    """
    Limits the number of words in a string.
    Usage: {{ some_text|limit_words:20 }}
    """
    words = value.split()[:int(arg)]
    return ' '.join(words)