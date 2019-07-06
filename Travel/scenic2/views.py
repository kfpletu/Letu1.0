from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.
def init_scenic(request):
    models.Scen.objects.create(sce_name='兵马俑',
                               sce_topic='秦始皇陵兵马俑', 
                               brief_des='世界八大奇迹之一,重现两千年前军队的姿态。',
                               address='陕西省西安市临潼区秦始皇陵以东1.5公里处',
                               assessment='乐途旅行口碑榜，最佳战略合作伙伴',
                               price=120,
                               cut_off_time='2019-10-10',
                               img='/static/images/scenic/information2/兵马俑.jpg'
                               )
    return HttpResponse(request,'information2.html',locals())
    # models.Scen.objects.create(sce_name='兵马俑',
    #                            sce_topic='秦始皇陵兵马俑', 
    #                            brief_des='世界八大奇迹之一,重现两千年前军队的姿态。',
    #                            address='陕西省西安市临潼区秦始皇陵以东1.5公里处',
    #                            assessment='乐途旅行口碑榜，最佳战略合作伙伴',
    #                            price='120',
    #                            cut_off_time='2019-10-10',
    #                            img='/static/images/scenic/information2/兵马俑.jpg'
    #                            )                           
    # models.Scen.objects.create(sce_name='兵马俑',
    #                            sce_topic='秦始皇陵兵马俑', 
    #                            brief_des='世界八大奇迹之一,重现两千年前军队的姿态。',
    #                            address='陕西省西安市临潼区秦始皇陵以东1.5公里处',
    #                            assessment='乐途旅行口碑榜，最佳战略合作伙伴',
    #                            price='120',
    #                            cut_off_time='2019-10-10',
    #                            img='/static/images/scenic/information2/兵马俑.jpg'
    #                            )
    # models.Scen.objects.create(sce_name='兵马俑',
    #                            sce_topic='秦始皇陵兵马俑', 
    #                            brief_des='世界八大奇迹之一,重现两千年前军队的姿态。',
    #                            address='陕西省西安市临潼区秦始皇陵以东1.5公里处',
    #                            assessment='乐途旅行口碑榜，最佳战略合作伙伴',
    #                            price='120',
    #                            cut_off_time='2019-10-10',
    #                            img='/static/images/scenic/information2/兵马俑.jpg'
    #                            )
    # models.Scen.objects.create(sce_name='兵马俑',
    #                            sce_topic='秦始皇陵兵马俑', 
    #                            brief_des='世界八大奇迹之一,重现两千年前军队的姿态。',
    #                            address='陕西省西安市临潼区秦始皇陵以东1.5公里处',
    #                            assessment='乐途旅行口碑榜，最佳战略合作伙伴',
    #                            price='120',
    #                            cut_off_time='2019-10-10',
    #                            img='/static/images/scenic/information2/兵马俑.jpg'
    #                            )
    # models.Scen.objects.create(sce_name='兵马俑',
    #                            sce_topic='秦始皇陵兵马俑', 
    #                            brief_des='世界八大奇迹之一,重现两千年前军队的姿态。',
    #                            address='陕西省西安市临潼区秦始皇陵以东1.5公里处',
    #                            assessment='乐途旅行口碑榜，最佳战略合作伙伴',
    #                            price='120',
    #                            cut_off_time='2019-10-10',
    #                            img='/static/images/scenic/information2/兵马俑.jpg'
    #                            )
    # models.Scen.objects.create(sce_name='兵马俑',
    #                            sce_topic='秦始皇陵兵马俑', 
    #                            brief_des='世界八大奇迹之一,重现两千年前军队的姿态。',
    #                            address='陕西省西安市临潼区秦始皇陵以东1.5公里处',
    #                            assessment='乐途旅行口碑榜，最佳战略合作伙伴',
    #                            price='120',
    #                            cut_off_time='2019-10-10',
    #                            img='/static/images/scenic/information2/兵马俑.jpg'
    #                            )
    # models.Scen.objects.create(sce_name='兵马俑',
    #                            sce_topic='秦始皇陵兵马俑', 
    #                            brief_des='世界八大奇迹之一,重现两千年前军队的姿态。',
    #                            address='陕西省西安市临潼区秦始皇陵以东1.5公里处',
    #                            assessment='乐途旅行口碑榜，最佳战略合作伙伴',
    #                            price='120',
    #                            cut_off_time='2019-10-10',
    #                            img='/static/images/scenic/information2/兵马俑.jpg'
    #                            )   
    # models.Scen.objects.create(sce_name='兵马俑',
    #                            sce_topic='秦始皇陵兵马俑', 
    #                            brief_des='世界八大奇迹之一,重现两千年前军队的姿态。',
    #                            address='陕西省西安市临潼区秦始皇陵以东1.5公里处',
    #                            assessment='乐途旅行口碑榜，最佳战略合作伙伴',
    #                            price='120',
    #                            cut_off_time='2019-10-10',
    #                            img='/static/images/scenic/information2/兵马俑.jpg'
    #                            )







