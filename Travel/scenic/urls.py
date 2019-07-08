from django.conf.urls import url
from . import views

#石霏霏 的url
urlpatterns = [
    #url(r'^adds1$',views.add_s1),
    #url(r'adds2$',views.add_s2),
    # url(r'^addtic$',views.add_tic),
    # url(r'^addintro$',views.add_intro),
    # url(r'^addmap$',views.add_map),
    # url(r'^addss$',views.add_s2),
    url(r'^$',views.index,name='scenic1'),
    url(r'^(\d+)/$',views.ticket),
    url(r'^scenic2$',views.scenic2,name='scenic2'),

]



#唐琳莎的url
urlpatterns +=[
    url(r'^scenic2',views.scenic2,name='scenic2'),
    url(r'^data1$', views.data1),
    url(r'^add_info',views.add_info),
    url(r'^add_desc',views.add_desc),
    url(r'^addtic$',views.add_ticket),
    url(r'^addintro',views.add_introduction),
    url(r'^addmap$',views.add_map),
]
