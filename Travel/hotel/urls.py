from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index,name='hotel'),
    url(r'^(\d+)$',views.hotel),
    # url(r'^init',views.init_house_id),#数据库导入专用路由
    # url(r'^copy',views.backup)#数据库备份专用路由
]
