from django.contrib import admin
from . import models
# Register your models here.
class InfoManage(admin.ModelAdmin):
    list_display = ['id', 'uname', 'phone', 'email', 'is_online']
    list_display_links = ['id', 'uname']
    list_filter = ['id']


admin.site.register(models.Info,InfoManage)
