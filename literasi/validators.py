import os
from django.core.validators import FileExtensionValidator
from django.forms import ValidationError

def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.pdf', '.mp3', '.mp4', '.mkv']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Hanya file dengan ekstensi pdf, mp3, mp4, dan mkv yang diizinkan.')