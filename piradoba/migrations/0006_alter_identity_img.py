# Generated by Django 3.2.8 on 2021-10-12 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('piradoba', '0005_auto_20211012_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='identity',
            name='img',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
