# Generated by Django 3.2.8 on 2021-10-13 22:28

from django.db import migrations, models
import piradoba.validators


class Migration(migrations.Migration):

    dependencies = [
        ('piradoba', '0008_alter_identity_personal_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='identity',
            name='img',
            field=models.ImageField(upload_to='images/', validators=[piradoba.validators.img_resolution]),
        ),
    ]
