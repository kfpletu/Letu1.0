# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-06-28 11:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0013_remove_room_room_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='room_level',
            field=models.CharField(default='1', max_length=5, verbose_name='房间编号'),
        ),
    ]