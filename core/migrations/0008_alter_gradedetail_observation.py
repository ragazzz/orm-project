# Generated by Django 4.1 on 2024-06-15 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_gradedetail_observation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gradedetail',
            name='observation',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]