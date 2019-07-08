#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/7/6 上午8:31
# @Author  : Kavin-lee
# @E-mail  :kavin_lee@yeah.net
# @FileName: views.py
# @Software: PyCharm
from django.shortcuts import render_to_response


def page_not_found(request):
    return render_to_response('404.html')