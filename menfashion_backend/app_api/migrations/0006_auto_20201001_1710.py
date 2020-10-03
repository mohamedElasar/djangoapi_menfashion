# Generated by Django 3.1.1 on 2020-10-01 14:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_api', '0005_auto_20201001_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favitems',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='my_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
