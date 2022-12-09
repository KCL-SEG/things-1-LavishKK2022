# Generated by Django 4.1.4 on 2022-12-09 13:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('things', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thing',
            name='description',
            field=models.TextField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='thing',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='thing',
            name='quantity',
            field=models.IntegerField(validators=[django.core.validators.MaxLengthValidator(100), django.core.validators.MinLengthValidator(0)]),
        ),
    ]