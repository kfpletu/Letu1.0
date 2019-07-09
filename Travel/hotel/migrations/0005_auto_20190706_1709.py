# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-07-06 17:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0004_room'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='jingdu',
            field=models.DecimalField(decimal_places=6, max_digits=9, null=True, verbose_name='经度'),
        ),
        migrations.AddField(
            model_name='hotel',
            name='weidu',
            field=models.DecimalField(decimal_places=6, max_digits=8, null=True, verbose_name='纬度'),
        ),
    ]