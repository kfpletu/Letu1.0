from django.conf.urls import url

from .views import *
#交通url分支
urlpatterns = [
    url(r'^$',trip_views),
    url(r'^search',search_views),
    url(r'^add_code',add_code_views),
]
