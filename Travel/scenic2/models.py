from django.db import models

# Create your models here.
class Scen(models.Model):
    sce_name=models.CharField('景点名称',max_length=8,unique=True,default='')
    sce_topic=models.CharField('主题名称',max_length=15,default='')
    brief_des=models.CharField('景点简述',max_length=40,default='')
    address=models.CharField('地址',max_length=40,default='')
    assessment=models.CharField('评价',max_length=100,default='')
    price=models.DecimalField("价格",max_digits=6,decimal_places=2,default=100)  
    cut_off_time=models.DateField("优惠截止时间",default='2019-09-20')
    img=models.ImageField('景点图片',null=True)
    # class Meta:
    #     verbose_name='景点信息表1'
    #     verbose_name_plural = verbose_name
    # def __str__(self):
    #     return (self.id,self.sce_name)

# class Scbr(models.Model):
#     sce_name = models.CharField('景点名称', max_length=8)
#     grage=models.CharField('景区级别',default='AAAA',max_length=10)
#     sce_addr=models.CharField("景区地址",max_length=30,null=True)
#     open_time=models.CharField("开放时间",max_length=200)
#     img1=models.ImageField('景点图片1')
#     img2=models.ImageField('景点图片2')
#     img3=models.ImageField('景点图片3')
#     img4=models.ImageField('景点图片4')
#     img5=models.ImageField('景点图片5')
#     word1=models.CharField('主题词1',max_length=5,null=True)
#     word2=models.CharField('主题词1',max_length=5,null=True)
#     scen=models.OneToOneField(Scen,models.CASCADE,null=True)
#     class Meta:
#         verbose_name='景点信息表2'
#         verbose_name_plural = verbose_name
# class Introduce(models.Model):
#     sce_details=models.TextField('景区介绍')
#     scbr=models.OneToOneField(Scbr,models.CASCADE,null=True)
# class Ticket(models.Model):
#     type=models.CharField("门票种类",max_length=10)
#     name=models.CharField("景点名称",max_length=20)
#     price=models.DecimalField("门票价格",max_digits=6,decimal_places=2)
#     scbr= models.ForeignKey(Scbr,models.CASCADE,null=True)
