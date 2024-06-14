import os
from django.core.validators import FileExtensionValidator
from django.forms import ValidationError

def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.jpg', '.jpeg', '.png', '.webp']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Hanya file dengan ekstensi jpg, jpeg, png, dan webp yang diizinkan.')