# Generated by Django 2.1.15 on 2022-05-14 02:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_recipe'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='time_munutes',
            new_name='time_minutes',
        ),
    ]
