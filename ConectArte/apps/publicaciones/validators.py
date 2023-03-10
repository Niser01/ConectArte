from django.core.exceptions import ValidationError

def file_size(value):
    filesize=value.size
    if filesize>2 * 1024 * 1024*25:
        raise ValidationError("maximum size is 50 mb")