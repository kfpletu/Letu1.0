from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$',views.index,name='scenic1'),
    url(r'^ticket',views.ticket,name='ticket'),
    url(r'^scenic2',views.scenic2,name='scenic2'),
    url(r'^adds1$',views.add_s1),
    url(r'^adds2$',views.add_s2),
    url(r'^addtic$',views.add_tic),
    url(r'^addintro$',views.add_intro),
]
