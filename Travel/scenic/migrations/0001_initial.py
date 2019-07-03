# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Introduce',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sce_details', models.TextField(verbose_name='景区介绍')),
            ],
        ),
        migrations.CreateModel(
            name='Scbr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sce_name', models.CharField(max_length=8, verbose_name='景点名称')),
                ('grage', models.CharField(default='AAAA', max_length=10, verbose_name='景区级别')),
                ('sce_addr', models.CharField(max_length=30, null=True, verbose_name='景区地址')),
                ('open_time', models.CharField(max_length=200, verbose_name='开放时间')),
                ('img1', models.ImageField(upload_to='', verbose_name='景点图片1')),
                ('img2', models.ImageField(upload_to='', verbose_name='景点图片2')),
                ('img3', models.ImageField(upload_to='', verbose_name='景点图片3')),
                ('img4', models.ImageField(upload_to='', verbose_name='景点图片4')),
                ('img5', models.ImageField(upload_to='', verbose_name='景点图片5')),
                ('word1', models.CharField(max_length=5, null=True, verbose_name='主题词1')),
                ('word2', models.CharField(max_length=5, null=True, verbose_name='主题词1')),
            ],
            options={
                'verbose_name': '景点信息表2',
                'verbose_name_plural': '景点信息表2',
            },
        ),
        migrations.CreateModel(
            name='Scen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sce_name', models.CharField(max_length=8, unique=True, verbose_name='景点名称')),
                ('sce_topic', models.CharField(max_length=15, verbose_name='主题名称')),
                ('brief_des', models.CharField(max_length=40, verbose_name='景点简述')),
                ('bus_go', models.CharField(max_length=40, verbose_name='公交')),
                ('car_go', models.CharField(max_length=40, verbose_name='自驾')),
                ('pre_price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='原价')),
                ('local_price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='现价')),
                ('low_time', models.DateField(default='2019-09-20', verbose_name='优惠截止时间')),
                ('img', models.ImageField(null=True, upload_to='', verbose_name='景点图片')),
            ],
            options={
                'verbose_name': '景点信息表1',
                'verbose_name_plural': '景点信息表1',
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=10, verbose_name='门票种类')),
                ('name', models.CharField(max_length=20, verbose_name='景点名称')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='门票价格')),
                ('scbr', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='scenic.Scbr')),
            ],
        ),
        migrations.AddField(
            model_name='scbr',
            name='scen',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='scenic.Scen'),
        ),
        migrations.AddField(
            model_name='introduce',
            name='scbr',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='scenic.Scbr'),
        ),
    ]
