from django.db import models


# Create your models here.

class Info(models.Model):
    uname = models.CharField('用户姓名', max_length=50,unique=True)
    upwd = models.CharField('用户密码', max_length=150,null=False)
    phone = models.CharField('手机号', max_length=11, unique=True)
    email = models.EmailField('邮箱')
    price = models.DecimalField('余额',max_digits=8,decimal_places=2,default=0)
    is_online = models.BooleanField('登录状态', default=0)
    join_time = models.DateTimeField('注册时间', auto_now_add=True)
    is_alive = models.BooleanField('是否注销', default=0)

    def __str__(self):
        return '姓名%s 电话%s 邮箱%s 余额%s 登录状态%s' \
        % (self.uname, self.phone, self.email, self.price, self.is_online)
    


class Cart(models.Model):
    user_id = models.IntegerField('用户id',db_index=True)
    g_img = models.ImageField('商品图片', upload_to='static/images')
    g_name = models.CharField('商品名称', max_length=50)
    time1 = models.CharField('时间1', max_length=50)
    time2 = models.CharField('时间2', max_length=50)
    g_type = models.CharField('商品类型', max_length=50)
    price = models.DecimalField('单价', max_digits=8, decimal_places=2)
    g_num = models.IntegerField('商品数量', default=1)
    total_price = models.DecimalField('总价', max_digits=10, decimal_places=2)
    add_time = models.DateTimeField(auto_now_add=True)
    is_pay = models.BooleanField(default=False)  # 默认0为未支付，1为已支付


class History_list(models.Model):
    u_id = models.IntegerField('用户id', db_index=True)
    g_img = models.ImageField('商品图片', upload_to='static/images')
    g_name = models.CharField('商品名称', max_length=50)
    time1 = models.CharField('时间1', max_length=50)
    time2 = models.CharField('时间2', max_length=50)
    g_type = models.CharField('商品类型', max_length=50)  # 1.表示酒店 2.表示景点 3.其他
    price = models.DecimalField('单价', max_digits=8, decimal_places=2)
    g_num = models.IntegerField('商品数量', default=1)
    total_price = models.DecimalField('总价', max_digits=10, decimal_places=2)
    booking_time = models.DateTimeField('订单时间', auto_now_add=True)
    serial_num = models.CharField('流水号', max_length=50)
    is_del = models.BooleanField(default=False)  # 默认0为删除，1为存在
