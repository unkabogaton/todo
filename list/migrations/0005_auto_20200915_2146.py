# Generated by Django 2.2.16 on 2020-09-15 13:46

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0004_auto_20200915_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='user',
            field=models.ForeignKey(default=django.contrib.auth.models.User, on_delete='models.CASCADE', to=settings.AUTH_USER_MODEL),
        ),
    ]
