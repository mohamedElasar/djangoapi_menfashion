# Generated by Django 3.1.1 on 2020-10-01 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_api', '0004_auto_20201001_0926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favitems',
            name='shops',
            field=models.ManyToManyField(blank=True, related_name='user_fav', to='app_api.Shop'),
        ),
    ]
