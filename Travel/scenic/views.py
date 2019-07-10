from django.shortcuts import render
from . import models
from django.http import HttpResponse, Http404, HttpResponseRedirect
from user.models import Cart, Info
import time, random
import datetime
import json


# Create your views here.

# 石霏霏的 views
def index(request):
    if request.method == 'GET':
        scens = models.Scen.objects.all()
        try:
            if hasattr(request, 'session') and 'userinfo' in request.session:
                uid = request.session['userinfo']['id']
                user = Info.objects.get(id=uid)
        except:
            raise Http404
        return render(request, 'scenic/information.html', locals())



def ticket(request, s):
    s = int(s)
    ts = models.Scbr.objects.get(id=s)
    tics = ts.ticket_set.all()
    stype=tics[0].type
    sname=tics[0].name
    sprice=tics[0].price
    stype2=tics[1].type
    sname2=tics[1].name
    sprice2=tics[1].price
    intr = ts.introduce.sce_details
    maps=ts.map
    jingdu=maps.jingdu
    weidu=maps.weidu
    if 'userinfo' not in request.session:
        return HttpResponseRedirect('/user/login')
    if request.method == 'GET':
        return render(request, 'scenic/ticket.html', locals())
    elif request.method == 'POST':
        if request.POST.get('sub') != '':
            retime = time.ctime()
            num=request.POST.get('number','')
            sttime=request.POST.get('starttime','')
            entime=request.POST.get('endtime','')
            stype=request.POST.get('stype')
            sname=request.POST.get('sname')
            sprice=request.POST.get('sprice')
            tprice=request.POST.get('tprice')
            ord=Cart.objects.create(
                                user_id=request.session['userinfo']['id'],
                                g_img=ts.img1,
                                g_name=sname,
                                time1= sttime,
                                time2= entime,
                                g_type=stype,
                                price= sprice,
                                g_num=num,
                                total_price=tprice,
                                add_time=retime,
                                serial_num=str(request.session['userinfo']['id']) +retime
                                        )
            now = retime
            from_data = sttime
            to_data = entime
            cart_id = str(request.session['userinfo']['id']) + now+str(random.uniform(5,10))
            return render(request,'scenic/booking.html',locals())

# def add_s1(request):
#     db1 = open('/home/tarena/Letu1.0/Travel/static/images/scenic/text/s1', 'r+', encoding='UTF-8')
#     for line in db1:
#         list1 = line.split('#')
#         if len(list1) == 10:
#             scens = models.Scen(id=list1[0], sce_name=list1[1], sce_topic=list1[2], brief_des=list1[3], bus_go=list1[4],
#                                 car_go=list1[5], pre_price=list1[6], local_price=list1[7], low_time=list1[8],
#                                 img=list1[9])
#             scens.save()
#     db1.close()
#     return HttpResponse('插入成功')


# def add_s2(request):
#     db2 = open('/home/tarena/Letu1.0/Travel/static/images/scenic/text/s2', 'r+', encoding='UTF-8')
#     for line in db2:
#         list2 = line.split('#')
#         if len(list2) == 13:
#             scen2 = models.Scbr(id=list2[0], sce_name=list2[1], grage=list2[2], sce_addr=list2[3], open_time=list2[4],
#                                 img1=list2[5], img2=list2[6], img3=list2[7], img4=list2[8], img5=list2[9],
#                                 word1=list2[10],
#                                 word2=list2[11], scen_id=list2[12])
#             scen2.save()
#     db2.close()
#     return HttpResponse('插入成功')


# def add_tic(request):
#     db3 = open('/home/tarena/Letu1.0/Travel/static/images/scenic/text/tic', 'r+', encoding='UTF-8')
#     for line in db3:
#         list3 = line.split('#')
#         if len(list3) == 5:
#             tic = models.Ticket(id=list3[0], type=list3[1], name=list3[2], price=list3[3], scbr_id=list3[4])
#             tic.save()
#     db3.close()
#     return HttpResponse('插入成功')


# def add_intro(request):
#     db4 = open('/home/tarena/Letu1.0/Travel/static/images/scenic/text/intr', 'r+', encoding='UTF-8')
#     data = ''
#     for line in db4:
#         data += line
#     list3 = data.split('###')
#     for i in range(len(list3)):
#         intro = models.Introduce(sce_details=list3[i])
#         intro.save()
#     db4.close()
#     return HttpResponse('插入成功')

# 唐琳莎的视图（views）
def data1(request):
    models.Scen2.objects.create(sce_name='兵马俑',
                                sce_topic='秦始皇陵兵马俑',
                                brief_des='世界八大奇迹之一,重现两千年前军队的姿态。',
                                address='陕西省西安市临潼区秦始皇陵以东1.5公里处',
                                assessment='乐途旅行口碑榜，最佳战略合作伙伴',
                                price=120,
                                cut_off_time='2019-10-10',
                                img='/static/images/scenic/information2/bingmayong.jpg'
                                )
    # return render(request,'scenic/information02.html',locals())
    return HttpResponse('ok')


def scenic2(request):
    scens = models.Scen2.objects.all()
    try:
        if hasattr(request, 'session') and 'userinfo' in request.session:
            uid = request.session['userinfo']['id']
            user = Info.objects.get(id=uid)
    except:
        raise Http404
    return render(request, 'scenic/information02.html', locals())


def add_info(request):
    db1 = open('/home/tarena/桌面/project/Letu1.0/Travel/static/images/scenic/text/scenic2_infor', 'r+', encoding='UTF-8')
    for text in db1:
        list = text.split('#')
        scens = models.Scen2(sce_name=list[8], sce_topic=list[2], brief_des=list[3],
                             address=list[4], assessment=list[5], price=list[7],
                             cut_off_time=list[6], img=list[1])
        scens.save()
    db1.close()
    return HttpResponse('插入成功')


def add_desc(request):
    db2 = open('/home/tarena/桌面/project/Letu1.0/Travel/static/images/scenic/text/scenic2_desc', 'r+', encoding='UTF-8')
    for line in db2:
        list2 = line.split('#')
        if len(list2) == 13:
            scen2 = models.Scbr(id=list2[0], sce_name=list2[1], grage=list2[2], sce_addr=list2[3],
                                open_time=list2[4], img1=list2[5], img2=list2[6], img3=list2[7],
                                img4=list2[8], img5=list2[9], word1=list2[10], word2=list2[11], scen_id=list2[12])
            scen2.save()
    db2.close()
    return HttpResponse('插入ok')


def add_ticket(request):
    db3 = open('/home/tarena/桌面/project/Letu1.0/Travel/static/images/scenic/text/ticket', 'r+', encoding='UTF-8')
    for line in db3:
        list3 = line.split('#')
        if len(list3) == 5:
            tic = models.Ticket(id=list3[0], type=list3[1], name=list3[2], price=list3[3], scbr_id=list3[4])
            tic.save()
        else:
            return HttpResponse('有错误')
    db3.close()
    return HttpResponse('插入成功')


def add_introduction(request):
    db4 = open('/home/tarena/桌面/project/Letu1.0/Travel/static/images/scenic/text/introduction', 'r+', encoding='UTF-8')
    data = ''
    for line in db4:
        data += line
    list3 = data.split('###')
    for i in range(len(list3)):
        intro = models.Introduce(sce_details=list3[i])
        intro.save()
    db4.close()
    return HttpResponse('插入成功')


def add_map(request):
    db5 = open('/home/tarena/桌面/project/Letu1.0/Travel/static/images/scenic/text/mapmap')
    for line in db5:
        list5 = line.split('#')
        if len(list5) == 4:
            maps = models.Map(id=list5[0], jingdu=list5[1], weidu=list5[2], scbr_id=list5[3])
            maps.save()
    db5.close()
    return HttpResponse('插入成功')
