import re

from django.core.exceptions import ValidationError



class NumberValidator(object):
    def validate(self, password, user=None):
        if not re.findall('\d', password):
            raise ValidationError(
                ("La contraseña debe contener al menos un número, 0-9."),
                code='password_no_number',
            )

    def get_help_text(self):
        return (
            "Su contraseña debe contener al menos 1 dígito, 0-9."
        )


class UppercaseValidator(object):
    def validate(self, password, user=None):
        if not re.findall('[A-Z]', password):
            raise ValidationError(
                ("La contraseña debe contener al menos 1 letra mayúscula, A-Z."),
                code='password_no_upper',
            )

    def get_help_text(self):
        return (
            "Su contraseña debe contener al menos 1 letra mayúscula, A-Z."
        )


class LowercaseValidator(object):
    def validate(self, password, user=None):
        if not re.findall('[a-z]', password):
            raise ValidationError(
                ("La contraseña debe contener al menos 1 letra minúscula, a-z."),
                code='password_no_lower',
            )

    def get_help_text(self):
        return (
            "Su contraseña debe contener al menos 1 letra minúscula, a-z."
        )


class SymbolValidator(object):
    def validate(self, password, user=None):
        if not re.findall('[()[\]{}|\\`~!@#$%^&*_\-+=;:\'",<>./?]', password):
            raise ValidationError(
                ("La contraseña debe contener al menos 1 símbolo: " +
                  "()[]{}|\`~!@#$%^&*_-+=;:'\",<>./?"),
                code='password_no_symbol',
            )

    def get_help_text(self):
        return (
            "Su contraseña debe contener al menos 1 símbolo: " +
            "()[]{}|\`~!@#$%^&*_-+=;:'\",<>./?"
        )