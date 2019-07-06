# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-07-06 09:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0003_auto_20190706_0947'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_name', models.CharField(max_length=20, verbose_name='房间名')),
                ('area', models.CharField(max_length=10, verbose_name='面积')),
                ('price', models.CharField(max_length=10, verbose_name='价位')),
                ('iprice', models.IntegerField(default=1, verbose_name='数字价位')),
                ('window', models.CharField(max_length=20, verbose_name='窗')),
                ('bed', models.CharField(max_length=100, verbose_name='床')),
                ('room_level', models.CharField(default='1', max_length=5, verbose_name='房间编号')),
                ('hotel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hotel.Hotel')),
                ('house', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hotel.House')),
            ],
            options={
                'db_table': 'room',
            },
        ),
    ]
