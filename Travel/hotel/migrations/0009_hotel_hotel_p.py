# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-06-27 10:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0008_auto_20190626_2021'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='hotel_p',
            field=models.CharField(default='/', max_length=25, verbose_name='图片地址'),
        ),
    ]
