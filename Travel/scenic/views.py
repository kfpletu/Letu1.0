from django.shortcuts import render
from . import models
from django.http import HttpResponse
import re

# Create your views here.
# Create your views here.
def index(request):
    if request.method=='GET':
        return render(request,'scenic/information.html')
def ticket(request):
    if request.method == 'GET':
        return render(request,'scenic/ticket.html')
def scenic2(request):
    if request.method == 'GET':
        return render(request,'scenic/information02.html')
def add_s1(request):
    db1=open('/home/tarena/Letu1.0/Travel/static/images/scenic/text/s1.txt','r+')
    for line in db1:
        list1 = line.split('#')
        scen1 = models.Scen(id=list1[0], sce_name=list1[1],sce_topic=list1[2], brief_des=list1[3], bus_go=list1[4],
                            car_go=list1[5],pre_price=list1[6],local_price=list1[7],low_time=list1[8])
        scen1.save()
    db1.close()
    return HttpResponse('插入成功')