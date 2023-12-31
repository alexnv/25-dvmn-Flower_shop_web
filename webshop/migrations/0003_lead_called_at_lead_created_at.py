# Generated by Django 4.1 on 2023-08-17 17:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webshop', '0002_lead'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='called_at',
            field=models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='дата звонка'),
        ),
        migrations.AddField(
            model_name='lead',
            name='created_at',
            field=models.DateTimeField(db_index=True, default=datetime.datetime.now, verbose_name='дата обращения'),
        ),
    ]
