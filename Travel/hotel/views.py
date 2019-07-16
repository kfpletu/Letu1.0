from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from . import models
from django.db.models import *
import os
import time
from django.conf import settings
from django.http import HttpResponseRedirect
from user.models import Cart, Info
from tools import weather
from django.core import serializers
from django.db.models import F


# 获得今天明天的日期
def get_time():
    today = time.strftime("%Y-%m-%d", time.localtime())
    tomorrow = time.strftime("%Y-%m-%d", time.localtime(time.time() + 86400))
    return today, tomorrow


# 天气预报
def city_weather(request):
    weather_str = weather.city_weather()
    return HttpResponse(weather_str + '这是天气信息,浏览信息请登录主页')


# def city_weather(request):
#     weather_str = weather.city_weather()
#     return HttpResponse(weather_str)


# hotel 预订首页
def index(request):
    if request.method == 'GET':
        today, tomorrow = get_time()
        try:
            if hasattr(request, 'session') and 'userinfo' in request.session:
                uid = request.session['userinfo']['id']
                user = Info.objects.get(id=uid)
        except:
            raise Http404
        return render(request, 'hotel/order_hotel.html', locals())
    elif request.method == 'POST':
        pass


#酒店首页酒店列表
def hotel_list(request):
    houses=models.House.objects.all().order_by('-order_count')
    houses=serializers.serialize('json',houses)
    return HttpResponse(houses)
    # houses




# 酒店价格首页
price_list = [(0, 200), (200, 500), (500, 1000), (1000, 2000), (2000, 10000), (0, 10000)]


# 关键字搜索
def search(keyword):
    if keyword:
        hotel = models.Hotel.objects.filter(
            Q(hotel_name__contains=keyword) | Q(address__contains=keyword) | Q(info__contains=keyword) | Q(
                hotel_level__contains=keyword))
        return hotel

hotel_level_list=[(10,19),(20,29),(30,39),(40,49),(50,59)]
# 酒店首页搜索引擎
def room(request):
    if request.method == 'GET':
        today, tomorrow = get_time()
        try:
            if hasattr(request, 'session') and 'userinfo' in request.session:
                uid = request.session['userinfo']['id']
                user = Info.objects.get(id=uid)
            #直接通过路由进入,显示全部房间
            if not request.GET:
                rooms = models.Room.objects.all()
                return render(request, 'hotel/order_room.html', locals())
            # 入住时间
            from_date = request.GET.get('from_date', '')
            # 退房时间
            to_date = request.GET.get('to_date', '')
            # 获取表单信息

            price = price_list[int(request.GET.get('room-price', ''))]
            print('prince',price)
            hotel_level = request.GET.get('hotel-level', '')
            keyword = request.GET.get('room-keyword', '')
            # 通过价位和人数找房间
            if request.GET['people-num'] == '1':
                rooms = models.Room.objects.filter(Q(iprice__range=price) & (Q(room_level=1) | Q(room_level=3)))
            else:
                rooms = models.Room.objects.filter(iprice__range=price)
            # 根据酒店级别筛选
            if hotel_level !='5':
                range=hotel_level_list[int(hotel_level)-1]
                rooms=rooms.filter(hotel_id__gte=range[0],hotel_id__lte=range[1])#hotel_level_list[int(hotel_level)-1])

            # 通过关键字找匹配酒店
            hotels = search(keyword)
            # print(hotels)
            if hotels:
                hotel_rooms=models.Room.objects.filter(hotel__in=hotels)
                # print(hotel_rooms)
                # rooms=rooms |hotel_rooms
            return render(request, 'hotel/order_room.html', locals())
        except:
            return HttpResponseRedirect('/hotel/')


# 导入酒店数据
def init_hotel(request):
    fd = open("/home/tarena/桌面/test/中期项目/Letu1.0/Travel/static/images/hotel/hotels.txt", 'r+')
    for line in fd:
        # line=fd.read()
        # line="32#'富力希尔顿大酒店'#'新城区东新街199号（近民乐园）'#'029-87388888'#'西安富力希尔顿酒店坐落于古城西安市中心，周边繁华购物区林立，是商务出行和休闲度假的理想之选。步行即可到达闻名于世的明城墙和西安地标建筑钟楼。乘坐出租车仅需5分钟即可到达东大街、骡马市步行街及回民街，这里有西安特色的餐厅、购物及娱乐场所。 拥有城中稀缺宽敞大容量客房，西安富力希尔顿酒店客房面积均大于43平方米。酒店高雅的客房别出心裁将唐朝元素融入其中，并突出了房间的温馨舒适。所有客房均配备高速宽带无线上网及高水准的客用品。 西安富力希尔顿酒店将成为您在西安的会议和用餐新选择。三间风格各异的餐厅及酒吧、一间1200平方米的大宴会厅及6间多功能厅可为您提供多种规模的会议及宴会需求。'#'星级酒店'"
        list = line.split('#')
        hotel = models.Hotel(id=list[0], hotel_name=list[1], address=list[2], phone=list[3], info=list[4],
                             hotel_level=list[5])
        hotel.save()
    fd.close()
    return HttpResponse('初始化成功')


# 初始化房间
def init_room(request):
    fd = open("/home/tarena/桌面/test/中期项目/Letu1.0/Travel/static/images/hotel/room.txt", 'r+')
    for line in fd:
        # line=fd.read()
        # line="32#'富力希尔顿大酒店'#'新城区东新街199号（近民乐园）'#'029-87388888'#'西安富力希尔顿酒店坐落于古城西安市中心，周边繁华购物区林立，是商务出行和休闲度假的理想之选。步行即可到达闻名于世的明城墙和西安地标建筑钟楼。乘坐出租车仅需5分钟即可到达东大街、骡马市步行街及回民街，这里有西安特色的餐厅、购物及娱乐场所。 拥有城中稀缺宽敞大容量客房，西安富力希尔顿酒店客房面积均大于43平方米。酒店高雅的客房别出心裁将唐朝元素融入其中，并突出了房间的温馨舒适。所有客房均配备高速宽带无线上网及高水准的客用品。 西安富力希尔顿酒店将成为您在西安的会议和用餐新选择。三间风格各异的餐厅及酒吧、一间1200平方米的大宴会厅及6间多功能厅可为您提供多种规模的会议及宴会需求。'#'星级酒店'"
        list = line.split('#')
        room = models.Room(room_name=list[0], area=list[1], price=list[2], window=list[3],
                           bed=list[4])
        room.save()
    fd.close()
    return HttpResponse('初始化成功')


# 导入图片地址
def house_p(request):
    houses = models.House.objects.all()
    for house in houses:
        a = house.id // 10
        b = house.id % 10
        house.hotel_p = "%s/%s" % (a, b)
        house.save()
    return HttpResponse('图片地址初始化')


# 备份房间数据
def backup(request):
    fd = open("/home/tarena/桌面/test/中期项目/Letu1.0/Travel/static/images/hotel/room.txt", 'r+')
    rooms = models.Room.objects.all()
    for room in rooms:
        str = room.room_name + '#' + room.area + '#' + room.price + '#' + room.window + '#' + room.bed + '\n'
        fd.write(str)
    fd.close()
    return HttpResponse('复制成功')


# 导入house表中hotel_p
def init_house_p():
    for house in models.House.objects.all():
        house.hotel_p = house.hotel.hotel_p
        house.save()


# 设置house_id
def init_house_id(request):
    models.Room.objects.all().update(house_id=F('hotel_id'))
    models.Hotel.objects.all().update(house_id=F('id'))
    return HttpResponse('初始化成功')


# 设置room_iprice
def init_house_iprice(requset):
    rooms = models.Room.objects.all()
    for room in rooms:
        room.iprice = int(room.price)
        room.save()
    return HttpResponse('价位设置成功')


# 数据库主表数据导入
def init_house(request):
    fd = open("/home/tarena/桌面/test/中期项目/Letu1.0/Travel/static/images/hotel/house.txt", 'r+')
    for line in fd:
        list = line.split('#')
        hotel = models.House(id=list[0], hotel_name=list[1])
        hotel.save()
    fd.close()
    return HttpResponse('初始化成功')


# 详情表数据函数
def hotel_ticket(id):
    id = int(id)
    hotel = models.Hotel.objects.get(id=id)
    order_count = hotel.house.order_count
    hotel_name = hotel.hotel_name  # '富力希尔顿大酒店'
    hotel_p = hotel.house.hotel_p
    phone = hotel.phone  # '029-87388888'
    address = hotel.address  # '新城区东新街199号（近民乐园）'
    infor = hotel.info  # '西安富力希尔顿酒店坐落于古城西安市中心，周边繁华购物区林立，是商务出行和休闲度假的理想之选。步行即可到达闻名于世的明城墙和西安地标建筑钟楼。乘坐出租车仅需5分钟即可到达东大街、骡马市步行街及回民街，这里有西安特色的餐厅、购物及娱乐场所。 拥有城中稀缺宽敞大容量客房，西安富力希尔顿酒店客房面积均大于43平方米。酒店高雅的客房别出心裁将唐朝元素融入其中，并突出了房间的温馨舒适。所有客房均配备高速宽带无线上网及高水准的客用品。 西安富力希尔顿酒店将成为您在西安的会议和用餐新选择。三间风格各异的餐厅及酒吧、一间1200平方米的大宴会厅及6间多功能厅可为您提供多种规模的会议及宴会需求。'
    rooms = hotel.room_set.all()
    longitude = hotel.jingdu
    latitude = hotel.weidu
    today, tomorrow = get_time()
    return locals()


# 计算住房天数
def count_days(from_date, to_date):
    from_date = from_date.split('-')
    to_date = to_date.split('-')
    if from_date[1] == to_date[1]:
        days = int(to_date[2]) - int(from_date[2])
    else:
        days = (int(to_date[1]) - int(from_date[1])) * 30 + int(to_date[2]) - int(from_date[2])
    return days


def map(request):
    if hasattr(request, 'session') and request.session['userinfo']:
        id = request.session['userinfo']['id']

    return HttpResponseRedirect('/hotel')


# 酒店详情视图函数
def hotel(request, id, level):
    dic = hotel_ticket(id)
    if request.method == 'GET':
        try:
            if hasattr(request, 'session') and 'userinfo' in request.session:
                uid = request.session['userinfo']['id']
                dic['user'] = Info.objects.get(id=uid)
        except:
            raise Http404
        return render(request, 'hotel/hotel_ticket.html', dic)
    elif request.method == 'POST':
        # print(type(request.body))
        # 将房间加入购物车
        try:
            # 创建流水号
            now = str(time.ctime())
            now_str = str(time.time()).split('.')
            now_str = now_str[1] + now_str[0]
            # print(request.session['userinfo']['id'])
            serial_num = str(request.session['userinfo']['id']) + \
                         now_str + id + level
            from_date = request.POST.get("from_date", '')
            to_date = request.POST.get("to_date", '')
            days = count_days(from_date, to_date)
            # 数据导入cart表
            Cart.objects.create(
                user_id=request.session['userinfo']['id'],
                g_img="/static/images/hotel/%s/2%s.png" % (
                    dic['hotel_p'], level),
                g_name=dic['hotel_name'],
                time1=from_date,
                time2=to_date,
                g_type=dic['rooms'][int(level) - 1].room_name,
                price=float(dic['rooms'][int(level) - 1].price) * days,
                total_price=float(dic['rooms'][int(level) - 1].price) * days,
                serial_num=serial_num
            )
            return render(request, 'hotel/booking.html', locals())
        except:
            return render(request, 'user/login.html')


# 商家文件上传
def upload_picture(request):
    if request.method == 'GET':
        return render(request, 'hotel/merchant.html')
    elif request.method == 'POST':
        # 得到文件流对象
        file = request.FILES['myfile']
        print('上传的文件名', file.name)
        level = request.POST.get('level', '')
        # 配置文件夹地址
        filename = os.path.join(os.path.join(settings.MEDIA_ROOT, level), file.name)
        with open(filename, 'wb') as f:
            f.write(file.file.read())
            return render(request, 'hotel/merchant.html', {'aa': '文件上传成功'})
    raise Http404


# 测试
def test(request):
    return render(request, 'hotel/order_room.html')
