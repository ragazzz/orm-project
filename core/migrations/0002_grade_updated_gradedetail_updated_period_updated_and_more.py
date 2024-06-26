# Generated by Django 4.1 on 2024-06-11 16:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='grade',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación'),
        ),
        migrations.AddField(
            model_name='gradedetail',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación'),
        ),
        migrations.AddField(
            model_name='period',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación'),
        ),
        migrations.AddField(
            model_name='professor',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación'),
        ),
        migrations.AddField(
            model_name='student',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación'),
        ),
        migrations.AddField(
            model_name='subject',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación'),
        ),
        migrations.AlterField(
            model_name='grade',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='gradedetail',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='period',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='professor',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='student',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='subject',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
