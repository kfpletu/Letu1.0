# -*- coding: utf-8 -*-
<<<<<<< HEAD
# Generated by Django 1.11.8 on 2019-07-02 18:48
# Generated by Django 1.11.8 on 2019-07-03 13:06
=======
>>>>>>> 73009b9dcf0f0d087b6b24cfe6bfb6deb7f878f4
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0014_room_room_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='iprice',
            field=models.IntegerField(default=1, verbose_name='数字价位'),
        ),
    ]
