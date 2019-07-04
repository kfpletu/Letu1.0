from django.conf.urls import url
from django.contrib import admin

from.import views

# 梦晗的路由
urlpatterns = [
    #url(r '^admin/', admin.site.urls),
    url(r'^login', views.login),
    url(r'^register', views.register),
    url(r'^forget$', views.getpwd),
    url(r'^getpwd$', views.updatepwd),
    url(r'^logout$', views.logout),
    url(r'^cancel$', views.cancel),
    url(r'^checkuname$', views.checkuname),
    url(r'^checkphone$', views.checkphone),
    url(r'^yanzma/$', views.yanzma),
]

# kavin的路由
urlpatterns += [
    url(r'^payment$', views.payment),
    url(r'^test', views.test), #用于测试
    url(r'^delete/', views.delete),
    url(r'^order$',views.order),
    url(r'^topUp$',views.topup),
    url(r'^top-top/$',views.top_top),
]

# 购物车的路由
urlpatterns += [
    url(r'^balance', views.balance),
    url(r'^cart', views.cart, name = 'goodType'),
    url(r'^booking$', views.booking),
    url(r'^del/(\d+)$', views.del_goods),
    url(r'^add/(\d+)$', views.add),
    url(r'^reduce/(\d+)$', views.reduce),
    url(r'^modif/(\d+)$', views.modif),
]