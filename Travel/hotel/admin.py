from django.contrib import admin
from . import models
# Register your models here.


class HotelManager(admin.ModelAdmin):
    list_display = ['id','hotel_name','address','jingdu','weidu']
    list_editable = ['jingdu','weidu']


class RoomManager(admin.ModelAdmin):
    list_display = ['id','room_name','hotel_id','house_id',"room_level"]
    list_editable = ['room_level']
    list_display_links=['room_name']
    list_filter = ['hotel_id']

class HouseManager(admin.ModelAdmin):
    list_display = ['id','hotel_name','order_count']
    list_editable = [ 'order_count']

admin.site.register(models.Hotel,HotelManager)
admin.site.register(models.Room,RoomManager)
admin.site.register(models.House,HouseManager)