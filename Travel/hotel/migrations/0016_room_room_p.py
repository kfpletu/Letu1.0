# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-07-02 19:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0015_room_iprice'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='room_p',
            field=models.CharField(default='1', max_length=50, verbose_name='房间图片地址'),
        ),
    ]
