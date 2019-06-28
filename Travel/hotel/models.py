from django.db import models

# Create your models here.



class House(models.Model):
    hotel_name=models.CharField('酒店名',max_length=20)
    house_count=models.IntegerField('剩余房间数量',default=30)
    order_count=models.IntegerField('下单次数',default=0)

    class Meta:
        db_table='house'

    def __str__(self):
        return '酒店名: %s 剩余房间数量:%s'%(self.hotel_name,self.house_count)


class Hotel(models.Model):
    hotel_name=models.CharField('酒店名字',max_length=20)
    address=models.CharField('酒店地址',max_length=100)
    phone=models.CharField('酒店电话',max_length=50)
    info=models.TextField('酒店详细信息')
    hotel_level=models.CharField('酒店级别',max_length=10)
    house=models.OneToOneField(House,models.CASCADE,null=True)
    hotel_p=models.CharField('图片地址',max_length=25,default='/')
    class Meta:
        db_table='hotel'


    def __str__(self):
        return "酒店名：%s 酒店电话：%s 酒店地址：%s"%(self.hotel_name,self.phone,self.address)


class Room(models.Model):
    room_name=models.CharField('房间名',max_length=20)
    area=models.CharField('面积',max_length=10)
    price=models.CharField('价位',max_length=10)
    window=models.CharField('窗',max_length=20)
    bed=models.CharField('床',max_length=100)
    hotel=models.ForeignKey(Hotel,null=True)
    house=models.ForeignKey(House,models.CASCADE,null=True)
    class Meta:
        db_table='room'

    def __str__(self):
        return '房间名: %s 价位: %s'%(self.room_name,self.price)

