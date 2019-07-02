from django.conf.urls import url
# from django.contrib import admin

from . import views
urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^login', views.login),
    url(r'^register', views.register),
    url(r'^cart',views.cart,name='goodType'),
    url(r'^order$',views.order),
    url(r'^forget$', views.getpwd),
    url(r'^getpwd$', views.updatepwd),
    url(r'^logout$', views.logout),
    url(r'^booking',views.booking),
    url(r'^topUp$', views.topup),
    url(r'^cancel$', views.cancel),
    url(r'^del/(\d+)$',views.del_goods),
    # url(r'^jump',views.jump),
    # url(r'history$',views.history),
    
    
]
