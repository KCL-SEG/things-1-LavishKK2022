from django.core.validators import MaxLengthValidator
from django.core.validators import MinLengthValidator
from django.db import models

class Thing(models.Model):
    name = models.CharField(max_length=30, unique=True, blank=False)
    description = models.TextField(max_length=120, blank=True)
    quantity = models.IntegerField(validators=[MaxLengthValidator(100), MinLengthValidator(0)])