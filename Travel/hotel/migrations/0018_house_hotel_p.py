# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-07-03 13:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0017_remove_room_room_p'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='hotel_p',
            field=models.CharField(default='/', max_length=25, verbose_name='图片地址'),
        ),
    ]