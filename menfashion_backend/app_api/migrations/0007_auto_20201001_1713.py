# Generated by Django 3.1.1 on 2020-10-01 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_api', '0006_auto_20201001_1710'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favitems',
            name='shops',
        ),
        migrations.AddField(
            model_name='favitems',
            name='shops',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_fav', to='app_api.shop'),
            preserve_default=False,
        ),
    ]
