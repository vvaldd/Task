from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate(self, min_length=8):
    # check for digit
    if not any(char.isdigit() for char in self):
        raise ValidationError(_('Password must contain at least 1 digit.'))

    # check for letter
    if not any(char.isalpha() for char in self):
        raise ValidationError(_('Password must contain at least 1 letter.'))

    # check for length
    if len(self) < min_length:
        raise ValidationError(_('Password must contain minimum 8 symbols.'))


