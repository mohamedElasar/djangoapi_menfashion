# Generated by Django 3.1.1 on 2020-10-03 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_api', '0010_auto_20201003_1703'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shop',
            name='owner',
        ),
    ]
