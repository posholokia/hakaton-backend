# Generated by Django 5.0.6 on 2024-06-01 13:46
from datetime import timedelta

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_subscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='duration',
            field=models.DurationField(default=timedelta(days=30), verbose_name='Продолжительность'),
            preserve_default=False,
        ),
    ]
