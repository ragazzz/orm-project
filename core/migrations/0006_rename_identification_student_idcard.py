# Generated by Django 4.1 on 2024-06-11 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_remove_period_year_period_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='identification',
            new_name='idcard',
        ),
    ]
