from django.shortcuts import render
from django.http import HttpResponse
from . import models
from django.db.models import *
import os
from . import weather
# Create your views here.
#酒店首页
def index(request):

    if request.method=='GET':
        weather_list=weather.city_weather()
        house_list=models.House.objects.order_by('-order_count')
        # for house in house_list:
        #     house.hotel.hotel_name=house.hotel_name
        #     house.hotel.save()
        house_list=house_list[0:9]#销量排名前9的酒店
        hotel_list=[]
        for house in house_list:
            hotel_list.append(house.hotel)
        house_list=house_list[0:5]#热门品牌
        return render(request,'hotel/order_hotel.html',locals())
    elif request.method=='POST':
        pass



# def test(requesst,x):
#     print(x)
#     return HttpResponse('测试成功%s'%x)
#导入酒店数据
def init_hotel(request):
            pwd=os.path.dirname(__file__)
            hotel_db_path=os.path.join(pwd,'db.txt')
            fd=open("/home/tarena/桌面/test/中期项目/letu/Travel/static/images/hotel/db2.txt",'r+')
            for line in fd:
                # line=fd.read()
                # line="32#'富力希尔顿大酒店'#'新城区东新街199号（近民乐园）'#'029-87388888'#'西安富力希尔顿酒店坐落于古城西安市中心，周边繁华购物区林立，是商务出行和休闲度假的理想之选。步行即可到达闻名于世的明城墙和西安地标建筑钟楼。乘坐出租车仅需5分钟即可到达东大街、骡马市步行街及回民街，这里有西安特色的餐厅、购物及娱乐场所。 拥有城中稀缺宽敞大容量客房，西安富力希尔顿酒店客房面积均大于43平方米。酒店高雅的客房别出心裁将唐朝元素融入其中，并突出了房间的温馨舒适。所有客房均配备高速宽带无线上网及高水准的客用品。 西安富力希尔顿酒店将成为您在西安的会议和用餐新选择。三间风格各异的餐厅及酒吧、一间1200平方米的大宴会厅及6间多功能厅可为您提供多种规模的会议及宴会需求。'#'星级酒店'"
                list=line.split('#')
                hotel=models.Hotel(id=list[0],hotel_name=list[1],address=list[2],phone=list[3],info=list[4],
                              hotel_level=list[5])
                hotel.save()
            fd.close()
            return HttpResponse('初始化成功')
#备份房间数据
def backup(request):
    fd = open("/home/tarena/桌面/test/中期项目/letu/Travel/static/images/hotel/room.txt", 'r+')
    rooms=models.Room.objects.all()
    for room in rooms:
        str=room.room_name+'#'+room.area+'#'+room.price+'#'+room.window+'#'+room.bed+'\n'
        fd.write(str)
    fd.close()
    return HttpResponse('复制成功')

#设置house_id
def init_house_id(request):
    models.Room.objects.all().update(house_id=F('hotel_id'))
    models.Hotel.objects.all().update(house_id=F('id'))
    return HttpResponse('初始化成功')

# 数据库主表数据导入
def init_house(request):
    fd = open("/home/tarena/桌面/test/中期项目/letu/Travel/static/images/hotel/house.txt", 'r+')
    for line in fd:
        list = line.split('#')
        hotel = models.House(id=list[0],hotel_name=list[1])
        hotel.save()
    fd.close()
    return HttpResponse('初始化成功')

#详情表函数
def hotel(request,id):
        id=int(id)
        order_count =models.House.objects.get(id=id).order_count
        hotel=models.Hotel.objects.get(id=id)
        hotel_name=hotel.hotel_name#'富力希尔顿大酒店'
        hotel_p=hotel.hotel_p
        phone=hotel.phone#'029-87388888'
        address=hotel.address#'新城区东新街199号（近民乐园）'
        infor=hotel.info#'西安富力希尔顿酒店坐落于古城西安市中心，周边繁华购物区林立，是商务出行和休闲度假的理想之选。步行即可到达闻名于世的明城墙和西安地标建筑钟楼。乘坐出租车仅需5分钟即可到达东大街、骡马市步行街及回民街，这里有西安特色的餐厅、购物及娱乐场所。 拥有城中稀缺宽敞大容量客房，西安富力希尔顿酒店客房面积均大于43平方米。酒店高雅的客房别出心裁将唐朝元素融入其中，并突出了房间的温馨舒适。所有客房均配备高速宽带无线上网及高水准的客用品。 西安富力希尔顿酒店将成为您在西安的会议和用餐新选择。三间风格各异的餐厅及酒吧、一间1200平方米的大宴会厅及6间多功能厅可为您提供多种规模的会议及宴会需求。'
        rooms=hotel.room_set.all()
        # print(rooms[0])
        # print(rooms[1])
        # print(rooms[2])
        room1_name=rooms[0].room_name
        room1_window=rooms[0].window
        room1_area=rooms[0].area
        room1_bed=rooms[0].bed
        room1_price=rooms[0].price
        room2_name= rooms[1].room_name
        room2_window=rooms[1].window
        room2_area= rooms[1].area
        room2_bed= rooms[1].bed
        room2_price= rooms[1].price
        room3_name= rooms[2].room_name
        room3_window=rooms[2].window
        room3_area= rooms[2].area
        room3_bed= rooms[2].bed
        room3_price= rooms[2].price
        return render(request,'hotel/hotel_ticket.html',locals())
