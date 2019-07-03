# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-07-02 19:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0014_merge_20190702_1829'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='serial_num',
            field=models.CharField(default='2019-01-01', max_length=50, verbose_name='流水号'),
        ),
        migrations.AlterField(
            model_name='history_list',
            name='booking_time',
            field=models.DateTimeField(verbose_name='订单时间'),
        ),
    ]