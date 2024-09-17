from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models

def validate_phone_number(value):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+0123456789'. Up to 11 digits allowed.")
    phone_regex(value)

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, validators=[validate_phone_number])
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.phone_number}'