from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$',views.index,name='scenic1'),
    url(r'^ticket',views.ticket,name='ticket'),
    url(r'^scenic2',views.scenic2,name='scenic2')
]
