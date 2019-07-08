def add_info():
    db1=open('../static/images/scenic/text/scenic2_infor','r+',encoding='UTF-8')
    for text in db1:
        list = text.split('#')
        print(list)
#         scens = models.Scen(sce_name=list[8],sce_topic=list[2],brief_des=list[3],
#                             address=list[4],assessment=list[5],price=list[7],
#                             cut_off_time=list[6],img=list[1])
#     #         scens.save()
#     # db1.close()乐途口碑榜最具影响力景区
#     # return HttpResponse('插入成功')
add_info()

# sce_name='兵马俑',
# sce_topic='秦始皇陵兵马俑',
# brief_des='世界八大奇迹之一,重现两千年前军队的姿态。',
# address='陕西省西安市临潼区秦始皇陵以东1.5公里处',
# assessment='乐途旅行口碑榜，最佳战略合作伙伴',
# price=120,
# cut_off_time='2019-10-10',
# img=