# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-07-06 15:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenic', '0003_auto_20190706_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scen2',
            name='address',
            field=models.CharField(default='', max_length=100, verbose_name='地址'),
        ),
    ]
