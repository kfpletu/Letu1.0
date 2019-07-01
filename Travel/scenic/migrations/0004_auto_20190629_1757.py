# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-06-29 17:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scenic', '0003_introduce_scbr_scen_ticket'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scbr',
            name='sce_add',
        ),
        migrations.AddField(
            model_name='introduce',
            name='scbr',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='scenic.Scbr'),
        ),
        migrations.AddField(
            model_name='scbr',
            name='sce_addr',
            field=models.CharField(max_length=30, null=True, verbose_name='景区地址'),
        ),
        migrations.AddField(
            model_name='scbr',
            name='scen',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='scenic.Scen'),
        ),
        migrations.AddField(
            model_name='scen',
            name='img',
            field=models.ImageField(null=True, upload_to='', verbose_name='景点图片'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='scbr',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='scenic.Scbr'),
        ),
        migrations.AlterField(
            model_name='scen',
            name='low_time',
            field=models.DateField(default='2019-09-20', verbose_name='优惠截止时间'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='name',
            field=models.CharField(max_length=20, verbose_name='景点名称'),
        ),
    ]