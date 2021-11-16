# Generated by Django 3.2.8 on 2021-10-12 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('piradoba', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='identity',
            old_name='personal_no',
            new_name='personal_number',
        ),
        migrations.AlterField(
            model_name='identity',
            name='birth_place',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='identity',
            name='first_name',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='identity',
            name='last_name',
            field=models.CharField(max_length=24),
        ),
    ]
