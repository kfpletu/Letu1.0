from django.db import models

# Create your models here.

class Info(models.Model):
    uname = models.CharField('用户姓名', max_length=15,unique=True)
    upwd = models.CharField('用户密码', max_length=15,null=False)
    phone = models.CharField('手机号', max_length=11, unique=True)
    email = models.EmailField('邮箱')


class Cart(models.Model):
    user_id = models.IntegerField('用户id')
    img = models.ImageField(upload_to='static/images')
    code1 = models.CharField('商品信息1',max_length=50)
    code2 = models.CharField('商品信息2',max_length=50)
    code3 = models.CharField('商品信息3',max_length=50)
    price_code = models.CharField('单价信息',max_length=50)
    price = models.DecimalField('单价',max_digits=8,decimal_places=2) 