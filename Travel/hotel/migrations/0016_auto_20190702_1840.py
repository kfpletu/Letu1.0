# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-07-02 18:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0015_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='cc',
        ),
        migrations.AddField(
            model_name='room',
            name='iprice',
            field=models.IntegerField(default=1, verbose_name='数字价位'),
        ),
    ]