# Generated by Django 3.1.1 on 2020-10-03 03:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_api', '0007_auto_20201001_1713'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShopOwner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='owner_shop', to='app_api.shop')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
