from django.contrib import admin
from . import models
# Register your models here.
class InfoManage(admin.ModelAdmin):
    list_display = ['id', 'uname', 'phone', 'email', 'is_online', 'join_time','is_alive']
    list_display_links = ['id', 'uname']
    list_filter = ['id']
class CartManage(admin.ModelAdmin):
    list_display = ['id','user_id','g_name']

admin.site.register(models.Info,InfoManage)
admin.site.register(models.History_list)
admin.site.register(models.Cart,CartManage)
