# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-07-03 13:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0016_room_room_p'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='room_p',
        ),
    ]