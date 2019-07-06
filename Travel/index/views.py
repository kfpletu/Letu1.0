from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, render_to_response, redirect
from django.http import Http404
# from ..scenic.models import *
# from ..hotel.models import *


# Create your views here.
from hotel.models import Hotel
from scenic.models import Scbr

from scenic.models import Scen


def index(request):
    uname = ''
    try:
        if hasattr(request,'session') and 'userinfo' in request.session:
            u_id = request.session['userinfo']['id']
            user=models.Info.objects.get(id=u_id)
        return render(request, 'index.html', locals())
    except:
        return render(request, 'index.html', locals())


def find(keyword):
    if keyword:
        values = Hotel.objects.filter(Q(hotel_name__contains=keyword)| Q(hotel_level__contains=keyword))
        return values


def find1(keyword):
    if keyword:
        values = Scbr.objects.filter(Q(sce_name__contains=keyword) | Q(sce_addr__contains=keyword) | Q(word1__contains=keyword) | Q(word2__contains=keyword))
        print(values)
        return values


def search(request):
    if request.method == "GET":
        search_s = request.GET['search']
        # 判断输入的关键词是否为酒店类的
        keyword_hotel = ['酒', '店', '酒店', '旅', '客栈', '房', '旅馆', '馆', '宾馆']
        keyword_scen = ['景', '门', '景点', '门票', '游', '旅游']
        keyword_trip = ['机票', '火', '车', '高铁', '车票', '汽车票', '游轮', '轮']
        # keyword_tickets = ['华清池', '大唐芙蓉园', '西安明城墙', '陕西历史博物馆', '小雁塔',
        #                    '秦陵地宫', '长恨歌', '秦岭野生动物园', '朱雀森林公园', '回民街',
        #                    '曲江海洋极地公园', '乐华城']
        # keyword_hotels_name = ['大麦酒店', '汉庭连锁酒店', '锦江之星', '美豪丽致酒店', '屋里厢民宿',
        #                        '谷雨小屋', '十里民宿', '富力希尔顿酒店', '西安开元名都酒店', '西安W酒店',
        #                        '西安凯悦酒店', '喜来登酒店', '爱屋情侣酒店', '花枝恋酒店', '米兰主题酒店',
        #                        '天鹅恋情情侣酒店'
        #                        ]
        if search_s in keyword_hotel:
            hotel = Hotel.objects.all()
            # house = House.objects.all()
            # room = Room.objects.all()
            data = {}
            for h in hotel:
                deatil = []
                deatil.append(h.house.hotel_p)
                deatil.append(h.hotel_name)
                deatil.append(h.info[0:50])
                deatil.append(h.address)
                deatil.append(h.hotel_level)
                for j in h.room_set.all():
                    deatil.append(j.price)
                    break
                deatil.append(h.id)
                data[h] = deatil
            return render(request, 'about/search.html', locals())
        # 判断输入的关键词是否为景点类
        elif search_s in keyword_scen:
            scen = Scbr.objects.all()
            ss = Scen.objects.all()
            data = {}
            for h in scen:
                deatil = []
                deatil.append(h.img1)
                deatil.append(h.sce_name)
                for s in ss:
                    deatil.append(s.brief_des[0:50])
                    break
                # deatil.append(h.scen.sce_topic)
                deatil.append(h.sce_addr)
                deatil.append(h.grage)
                for s in ss:
                    deatil.append(s.local_price)
                    break
                deatil.append(h.id)
                data[h] = deatil

            return render(request, 'about/search1.html', locals())
        # 判断输入的关键词是否有车票类
        elif search_s in keyword_trip:
            return redirect('/trip')
        elif find(search_s):
            data1 = find(search_s)
            data = {}
            for h in data1:
                deatil = []
                deatil.append(h.house.hotel_p)
                deatil.append(h.hotel_name)
                deatil.append(h.info[0:50])
                deatil.append(h.address)
                deatil.append(h.hotel_level)
                for j in h.room_set.all():
                    deatil.append(j.price)
                    break
                deatil.append(h.id)
                data[h] = deatil
            return render(request, 'about/search.html', locals())
        elif find1(search_s):
            scen = find1(search_s)
            print(scen)
            ss = Scen.objects.all()
            data = {}
            for h in scen:
                deatil = []
                deatil.append(h.img1)
                deatil.append(h.sce_name)
                for s in ss:
                    deatil.append(s.brief_des[0:50])
                    break
                deatil.append(h.sce_addr)
                deatil.append(h.grage)
                for s in ss:
                    deatil.append(s.local_price)
                    break
                deatil.append(h.id)
                data[h] = deatil

            return render(request, 'about/search1.html', locals())
    elif request.method == "POST":
        pass
