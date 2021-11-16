# Generated by Django 3.2.8 on 2021-10-12 15:05

from django.db import migrations, models
import piradoba.validators


class Migration(migrations.Migration):

    dependencies = [
        ('piradoba', '0002_auto_20211012_1835'),
    ]

    operations = [
        migrations.AddField(
            model_name='identity',
            name='gender',
            field=models.CharField(default='', max_length=6, validators=[piradoba.validators.gender_choices]),
        ),
    ]