from django.conf.urls import url
# from django.contrib import admin

from . import views
urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url('^$', views.index),
    url(r'^index', views.index),

    
]
