from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect

from user.models import Info
from .trail_12306 import *
from . import models
import time


# Create your views here.
def trip_views(request):
    today = time.strftime("%Y-%m-%d", time.localtime())
    tomorrow = time.strftime("%Y-%m-%d", time.localtime(time.time() + 86400))
    try:
        if hasattr(request, 'session') and 'userinfo' in request.session:
            uid = request.session['userinfo']['id']
            user = Info.objects.get(id=uid)
    except:
        raise Http404
    return render(request, 'trip/order.html', locals())


def add_code_views(request):
    """
    增加12306车站数据
    :param request:
    :return:
    """
    tt = TicketQuery()
    station_code = tt.get_station_name()[0]
    for station_name, code in station_code.items():
        models.Trip.objects.create(station_name=station_name, station_code=code)
    return HttpResponse('OK')


def search_views(request):
    """
    爬取12306车票信息
    :param request:
    :return:
    """
    if request.method == "GET":
        from_station = request.GET.get('from_city', '')
        to_station = request.GET.get('to_city', '')
        from_date = request.GET.get('from_day', '')
        to_date = request.GET.get('to_day', '')
        # print(type(from_station))
        # print(from_station,to_station,from_date,to_date)
        tt = TicketQuery()
        data = tt.query(from_station, to_station, from_date)
        print(data)
        try:
            if hasattr(request, 'session') and 'userinfo' in request.session:
                uid = request.session['userinfo']['id']
                user = Info.objects.get(id=uid)
        except:
            raise Http404
        return render(request, 'trip/new_order.html', locals())
    elif request.method == "POST":
        return HttpResponse("没有这项服务")
