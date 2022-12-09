from django.core.validators import MaxLengthValidator
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError
from django.db import models

def valid_range(value):
    if value < 0 or value > 100:
        raise ValidationError('value is not within the range!')


class Thing(models.Model):
    name = models.CharField(max_length=30, unique=True, blank=False)
    description = models.CharField(max_length=120, blank=True)
    quantity = models.IntegerField(blank=False, validators=[valid_range])