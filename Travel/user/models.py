from django.db import models

# Create your models here.

class Info(models.Model):
    uname = models.CharField('用户姓名', max_length=15,unique=True)
    upwd = models.CharField('用户密码', max_length=15,null=False)
    phone = models.CharField('手机号', max_length=11, unique=True)
    email = models.EmailField('邮箱')


class Cart(models.Model):
    user_id = models.IntegerField('用户id')
    g_img = models.ImageField('商品图片',upload_to='static/images')
    g_name = models.CharField('商品名称',max_length=50)
    time1 = models.CharField('时间1',max_length=50)
    time2 = models.CharField('时间2',max_length=50)
    g_type = models.CharField('商品类型',max_length=50)
    price = models.DecimalField('单价',max_digits=8,decimal_places=2)
    g_num = models.IntegerField('商品数量',default=1)
    total_price = models.DecimalField('总价',max_digits=10,decimal_places=2)
    add_time = models.DateTimeField(auto_now_add=True)
    is_pay = models.BooleanField(default=False)  #默认0为未支付，1为已支付  
