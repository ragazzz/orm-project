# Generated by Django 4.1 on 2024-06-11 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_period_name_period_end_date_period_start_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='period',
            name='year',
        ),
        migrations.AddField(
            model_name='period',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
