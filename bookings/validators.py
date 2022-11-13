from django.core.validators import ValidationError

def validate_is_alpha(value):
    if value.isalpha():
        return value
    raise ValidationError(message="Name should not contain any digits.")