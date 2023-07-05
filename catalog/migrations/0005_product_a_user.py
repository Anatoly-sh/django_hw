# Generated by Django 4.2.1 on 2023-07-03 15:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0004_version'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='a_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='авторизованный пользователь'),
        ),
    ]