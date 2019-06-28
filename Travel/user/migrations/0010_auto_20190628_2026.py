# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-06-28 20:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='History_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_id', models.IntegerField(db_index=True, verbose_name='用户id')),
                ('g_img', models.ImageField(upload_to='static/images', verbose_name='商品图片')),
                ('g_name', models.CharField(max_length=50, verbose_name='商品名称')),
                ('time1', models.CharField(max_length=50, verbose_name='时间1')),
                ('time2', models.CharField(max_length=50, verbose_name='时间2')),
                ('g_type', models.CharField(max_length=50, verbose_name='商品类型')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='单价')),
                ('g_num', models.IntegerField(default=1, verbose_name='商品数量')),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='总价')),
                ('booking_time', models.DateTimeField(auto_now_add=True, verbose_name='订单时间')),
                ('serial_num', models.CharField(max_length=50, verbose_name='流水号')),
                ('is_del', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='cart',
            name='user_id',
            field=models.IntegerField(db_index=True, verbose_name='用户id'),
        ),
    ]
