from django.conf.urls import url

from about.views import *

urlpatterns = [
    url(r'^$',about_views),
    url(r'^travelContract$',travelContract_views),
    url(r'^childPrice$',childPrice_views),
    url(r'^touristRoute$',touristRoute_views),
    url(r'^singleRoom$',singleRoom_views),
    url(r'^travelInsuranceCategory$',travelInsuranceCategory_views),
]
