from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index,name='hotel'),
    url(r'^(\d+)/(\d?)',views.hotel,name='room'),
    url('^room$',views.room),
    url('^weather/$',views.city_weather),
    # url(r'^init',views.init_house_id),#数据库导入专用路由
    # url(r'^copy',views.backup)#数据库备份专用路由
    # url(r'book',views.test_book)#测试路由
    # url(r'upload_picture',views.upload_picture)#商家文件上传
    # url(r'^test',views.init_house_iprice)#测试数据库
]
