# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-07-06 09:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenic', '0002_map'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='map',
            name='add',
        ),
        migrations.AddField(
            model_name='map',
            name='jingdu',
            field=models.DecimalField(decimal_places=6, max_digits=9, null=True, verbose_name='经度'),
        ),
        migrations.AddField(
            model_name='map',
            name='weidu',
            field=models.DecimalField(decimal_places=6, max_digits=8, null=True, verbose_name='纬度'),
        ),
    ]
