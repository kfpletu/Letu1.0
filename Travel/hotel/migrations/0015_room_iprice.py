# -*- coding: utf-8 -*-
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
