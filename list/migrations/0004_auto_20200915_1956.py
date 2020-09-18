# Generated by Django 2.2.16 on 2020-09-15 11:56

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0003_item_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='user',
            field=models.ForeignKey(on_delete='models.CASCADE', to=settings.AUTH_USER_MODEL),
        ),
    ]