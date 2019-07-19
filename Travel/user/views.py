import hashlib
import json
import os
import random
import time

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
from django.conf import settings
from django.core.paginator import Paginator
from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from PIL import Image, ImageDraw, ImageFont

from tools.ssm_tx import ssm
# 订单结算                                
from hotel.models import House

from tools.send_email import SendMail
from .models import *

import redis

def pwd_hash(passwd):
    # 将密码进行hash
        s = 'letuTravel'
        h_p = hashlib.sha1()
        s_p = hashlib.sha1()   
        h_p.update(passwd.encode())
        s_p.update(s.encode())
        upwd = h_p.hexdigest() + s_p.hexdigest()
        h_p = hashlib.sha1()
        h_p.update(upwd.encode())
        upwd = h_p.hexdigest()
        return upwd

# 登录
def login(request):
    if request.method == 'GET':
        return render(request, 'user/login.html')
    elif request.method == 'POST':
        # 获取登录页面form表单提交的uname和upwd,并将upwd进行hash加密
        uname = request.POST.get('uname')
        upwd = request.POST.get('upwd')
        upwd = pwd_hash(upwd)
        try:
            # 从数据库获取uname和upwd
            user = Info.objects.get(uname=uname, upwd=upwd)
        except Exception as e:
            # 出异常,说明用户名密码不正确,刷新当前登录页面
            return HttpResponse('登录失败,请重新登录')
        # 登录状态为真,刷新登录页面,禁止登录
        if user.is_alive:
            resp = HttpResponse('该用户已经注销')
            return resp
        else:
            if user.is_online:
                resp = HttpResponse('该用户已在其他地方登录')
                return resp
            else:
                # 修改登录状态,发送seesion,返回首页
                user.is_online = 1
                user.save()
                request.session['userinfo'] = {
                    'uname': user.uname,
                    'id': user.id
                }
                resp = HttpResponse('登录成功', locals())
                return resp


# 图片验证码
def yanzma(request):
    """
        登录图形图形验证码
    """
    img = Image.new("RGB", (110, 37), (255, 255, 255))
    code = [chr(x) for x in range(97, 122)] + [str(x) for x in range(2, 10)] + [chr(x) for x in range(65, 90)]
    code = random.sample(code, 6)
    code = ''.join(code)
    draw = ImageDraw.Draw(img)
    for _ in range(10):
        draw.point(
            (random.randint(0, 110), random.randint(0, 37)),  # 坐标
            fill=(0, 0, 0))  # 颜色
    for _ in range(10):
        draw.line([(random.randint(0, 110), random.randint(0, 37)),
        (random.randint(0, 110), random.randint(0, 37))],
                  fill=(150, 150, 2))

    font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSerif.ttf", 24)
    draw.text((5, 5), code, font=font, fill="green")
    src = 'static/images/logImg/code.jpg'
    img.save(src)
    src = '/static/images/logImg/code.jpg'
    imgUrl = {
        'url': src,
        'code': code
    }
    return HttpResponse(json.dumps(imgUrl))


# 手机验证码登录
def phoneLogin(request):
    if request.method == 'GET':
        return render(request, 'user/phoneLogin.html')
    elif request.method == 'POST':
        phone = request.POST.get('phone')
        try:
            # 从数据库获取phone
            user = Info.objects.get(phone=phone)
            # 登录状态为真,刷新登录页面,禁止登录
            if user.is_alive:
                resp = HttpResponse('该用户已经注销')
                return resp
            else:
                if user.is_online:
                    resp = HttpResponse('该用户已在其他地方登录')
                    return resp
                else:
                    # 修改登录状态,发送seesion,cookie,返回首页

                    request.session['userinfo'] = {
                        'uname': user.uname,
                        'id': user.id
                    }
                    user.is_online = 1
                    user.save()
                    return HttpResponse('', locals())
        except:
            # 出异常,说明用户名密码不正确,刷新当前登录页面
            return HttpResponse('1')


# 检测登录手机是否注册
def check_phone_login(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        if not Info.objects.filter(phone=phone):
            jsonStr = {
                'mes': '手机号没有注册'
            }
        else:
            jsonStr = {
                'mes': ''
            }
        return HttpResponse(json.dumps(jsonStr))


# 获取登录验证码
def getMes(request):
    phone = request.GET.get('phone')
    number = random.randint(100000, 999999)
    phone_check(phone, "SMS_169902712", number)
    jsonStr = {
        'num': number
    }
    return HttpResponse(json.dumps(jsonStr))


# 发送手机验证码
def phone_check(phone, code, number):
    client = AcsClient('LTAIxo8uU7FoZPog',
                       '5fhRNu2256WxUF5dP9QdSmqqbZ50ul', 'cn-hangzhou')
    request = CommonRequest()
    request.set_accept_format('json')
    request.set_domain('dysmsapi.aliyuncs.com')
    request.set_method('POST')
    request.set_protocol_type('https')  # https | http
    request.set_version('2017-05-25')
    request.set_action_name('SendSms')

    request.add_query_param('RegionId', 'cn-hangzhou')
    request.add_query_param('PhoneNumbers', phone)
    request.add_query_param('SignName', "letu")
    request.add_query_param('TemplateCode', code)
    request.add_query_param('TemplateParam', "{'code':%s}" % number)

    response = client.do_action(request)
    print(str(response, encoding='utf-8'))


# 注册
def register(request):
    if request.method == 'GET':
        return render(request, 'user/register.html')
    elif request.method == 'POST':
        # 获取用户注册输入的信息,并将密码进行hash加密
        uname = request.POST.get('uname')
        upwd = request.POST.get('upwd')
        upwd = pwd_hash(upwd)
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        # 尝试向数据库添加用户信息,成功返回到登录页面进行登录
        try:
            Info.objects.create(uname=uname, upwd=upwd, phone=phone, email=email,
                                head_img='head.jpg')
            return HttpResponse('')
        except Exception as e:
            # 抛异常,刷新注册页面,重新注册
            return HttpResponse('注册失败,请重新注册')


# 检测当前用户名是否被注册
def checkuname(request):
    uname = request.GET.get('uname')
    if Info.objects.filter(uname=uname):
        return HttpResponse('用户名已经存在')
    return HttpResponse('')


# 检测当前手机号是否被注册
def checkphone(request):
    phone = request.GET.get('phone')
    if Info.objects.filter(phone=phone):
        return HttpResponse('该手机号码已经被注册')
    return HttpResponse('')


# 注册短信验证码
def message(request):
    phone = request.GET.get('phone')
    number = random.randint(100000, 999999)
    phone_check(phone, "SMS_169897609", number)
    jsonStr = {
        'num': number
    }
    return HttpResponse(json.dumps(jsonStr))


# 忘记密码
def getpwd(request):
    if request.method == 'GET':
        return render(request, 'user/forget.html')
    elif request.method == 'POST':
        # 获取用户输入的信息
        uname = request.POST.get('uname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        # 将用户输入的信息与数据库进行比对,正确则发送seesion,返回重置密码页面
        try:
            info = Info.objects.get(uname=uname, phone=phone, email=email)
            request.session['uname'] = info.uname
            return HttpResponse('')
        except:
            # 抛异常则输入信息不正确,刷新忘记密码页面
            return HttpResponse('输入信息有误,请重新输入')


# 修改密码
def updatepwd(request):
    if request.method == 'GET':
        return render(request, 'user/forget_new.html')
    elif request.method == 'POST':
        # 获取用户输入的新密码
        new_pwd = request.POST.get('new_pwd')
        upwd = pwd_hash(new_pwd)

        try:
            uname = request.session['uname']
            # 修改相应用户的密码,删除seesion,返回登录页面
            abook = Info.objects.get(uname=uname)
            abook.upwd = upwd
            abook.save()
            del request.session['uname']
            return HttpResponse('ok')
        except:
            # 重新返回忘记密码页面
            return HttpResponse('')

# 退出登录
def logout(request):
    try:
        # 获取seesion中的id信息,修改对应id的用户登录状态修改,删除session,返回首页
        uid = request.session['userinfo']['id']
        user = Info.objects.get(id=uid)
        user.is_online = False
        user.save()
        del request.session['userinfo']
        return HttpResponseRedirect('/')
    except:
        # 直接返回首页,但不删除seesion
        return HttpResponseRedirect('/')


# 注销登录
def cancel(request):
    try:
        # 获取seesion中的id信息,修改对应id的用户登录状态,删除session,返回首页
        uid = request.session['userinfo']['id']
        user = Info.objects.get(id=uid)
        user.is_online = False
        # 修改用户注销状态
        user.is_alive = True
        user.save()
        del request.session['userinfo']
        return HttpResponse('login')
    except:
        # 直接返回首页,但不删除seesion
        return HttpResponseRedirect('')


# 订购成功跳转页面
def booking(request):
    return render(request, 'user/booking.html', locals())


# 购物车
def cart(request):
    try:
        u_id = request.session['userinfo']['id']
    except:
        return render(request,'user/login.html')
    # 获取用户对象
    balance = Info.objects.get(id=u_id)
    # 获取该用户购物车商品对象
    goods = Cart.objects.filter(user_id=u_id, is_pay=0).order_by("-add_time")
    paginator = Paginator(goods, 4)
    cur_page = request.GET.get('page', 1)
    page = paginator.page(cur_page)
    return render(request, 'user/cart.html', locals())


# 历史记录
def order(request):
    try:
        uid = request.session['userinfo']['id']
    except:
        return render(request,'user/login.html')
    user = Info.objects.get(id=uid)
    datas = History_list.objects.filter(u_id=uid, is_del='1').order_by('-booking_time')
    paginator = Paginator(datas, 4)
    cur_page = request.GET.get('page', 1)
    page = paginator.page(cur_page)
    return render(request, 'user/order.html', locals())


# 删除购物车商品
def del_goods(request, g_id, num):
    target = Cart.objects.get(id=g_id)
    target.delete()
    try:
        u_id = request.session['userinfo']['id']
    except:
        return render(request,'user/login.html')
    # 获取用户对象
    balance = Info.objects.get(id=u_id)
    goods = Cart.objects.filter(user_id=u_id, is_pay=0).order_by("-add_time")
    paginator = Paginator(goods, 4)
    num = int(num)
    print('我是num:',num)
    print('啦啦啦',(paginator.count)%4)
    if (paginator.count)%4==0:
        print('哈哈哈哈')
        page = paginator.page(num-1)
    else:
        page = paginator.page(num)
    return render(request, 'user/cart.html', locals())


# 数量加1
def add(request, g_id):
    target = Cart.objects.get(id=g_id)
    n = target.g_num
    p = target.price
    n += 1
    total_p = p * n
    target.total_price = total_p
    target.g_num = n
    target.save()
    return render(request, 'user/cart.html')


# 数量减1
def reduce(request, g_id):
    target = Cart.objects.get(id=g_id)
    n = target.g_num
    p = target.price
    if n > 1:
        n -= 1
    total_p = p * n
    target.total_price = total_p
    target.g_num = n
    target.save()
    return render(request, 'user/cart.html')

#结算
def modif(request, g_id):
    '''订单结算'''
    target = Cart.objects.get(id=g_id)
    target.is_pay = 1
    target.save()

     #购买成功生成历史订单
    try:
        History_list.objects.create(
            u_id=target.user_id,
            g_img=target.g_img,
            g_name=target.g_name,
            time1=target.time1,
            time2=target.time2,
            g_type=target.g_type,
            price=target.price,
            g_num=target.g_num,
            total_price=target.total_price,
            booking_time='2018-3-3',
            is_del=target.is_pay
        )
        #酒店结算
        house_id = int(str(target.g_img)[-8]) + int(str(target.g_img)[-10]) * 10
        #成交短信

        user_key='user'+str(target.user_id)
        target_id = 'target' + str(target.id)
        #将订单id加入到用户id的列表中
        redis.Redis().lpush(user_key,target_id)
        phone=Info.objects.get(id=target.user_id).phone
        g_name=target.g_name
        g_type=target.g_type
        menoy=str(target.total_price)[0:-1]
        from_time=target.time1
        #将电话，金额等属性生产以订单id哈希映射中
        redis.Redis().hmset(target_id,{'phone':phone,'g_name':g_name,
                                            'g_type':g_type,'menoy':menoy,'from_time':from_time})

    except:
        return HttpResponse('购买失败')
    else:
        return HttpResponse('payment.html')

#支付成功页面发短信
def payment_ssm(request):
    if hasattr(request, 'session') and 'userinfo' in request.session:
        u_id = request.session['userinfo']['id']
        #根据用户键，得到订单keys
        r=redis.Redis().lrange('user'+str(u_id),0,-1)
        # print('r',r)
        for i in range(len(r)):
            #取出一个订单
            target_id=r.pop().decode()
            #根据订单id，找到订单哈希
            dict=redis.Redis().hgetall(target_id)
            # print(dict)
            phone=dict[b'phone'].decode()
            g_name=dict[b'g_name'].decode()
            g_type=dict[b'g_type'].decode()
            menoy=dict[b'menoy'].decode()
            from_time=dict[b'from_time'].decode()
            print(phone,g_name,g_type,menoy,from_time)
            result=ssm(phone,g_name,g_type,menoy,from_time)
            print(result)
            redis.Redis().delete(target_id)

        return JsonResponse({'code':'200','data':'ok'})
    else:
        return HttpResponseRedirect('/')




# 支付成功跳转页面
def payment(request):
    """
    支付界面的返回
    :param request:
    :return:
    """
    uid = request.session['userinfo']['id']
    user = Info.objects.get(id=uid)
    return render(request, 'user/payment.html', locals())




def test(request):
    """用于测试"""
    History_list.objects.create(
        u_id=85,
        g_img='/static/images/scenic/info/a1.jpg',
        g_name='华清池',
        time1='2019-07-02',
        time2='2019-07-02',
        g_type=2,
        price=70,
        g_num=1,
        total_price=70,
        booking_time='2019-07-02 15:55:30.854756',
        serial_num=2019454821548412,
        is_del=True
    )
    return HttpResponse("ok")


def topup(request):
    """
    :param request:
    :return:
    """
    u_id = request.session['userinfo']['id']
    user = Info.objects.get(id=u_id)
    price = float(user.price)
    return render(request, 'pay/topUp.html', locals())


def top_top(request):
    """
    充值金额的实现
    :param request:
    :return: 布尔值
    """
    uid = request.session['userinfo']['id']
    user = Info.objects.get(id=uid)
    money = float(request.POST['money'])
    try:
        change_money = float(user.price)
        change_money = change_money + money
        user.price = change_money
        user.save()
        time1=time.strftime('%Y-%m-%d %H:%M:%S')
        content = '亲爱的乐途用户,您在 %s 成功充值 %s 元,您的可用余额为 %s 元。' \
                  '努力,让旅行变得更简单,让旅行变得更享受,让您乐在途中![乐途旅行网]' % (time1,money,change_money)
        to_user = user.email
        send = SendMail(username='360679877@qq.com',
                              passwd='mzawjnawwpzxbicj',
                              recv=to_user,
                              title='[余额变动通知]',
                              content=content,
                              file=None,
                              ssl=True, )
        send.send_mail()
        return HttpResponse("1")
    except:
        return HttpResponse("0")


# 删除历史订单
def delete(request):
    """
    用户删除自己的购买记录
    :param request: 前端的请求
    :return:
    """
    id = request.GET['id']
    num = request.GET['num']
    data = History_list.objects.filter(id=id)
    data.update(is_del=0)
    user_id = request.session['userinfo']['id']
    order = History_list.objects.filter(u_id=user_id, is_del=1).order_by('-booking_time')
    paginator = Paginator(order, 4)
    page = paginator.page(num)
    return render(request, 'user/order.html', locals())


# 余额
def balance(request):
    t_price = request.GET["totalPrice"]
    t_price = int(t_price)
    u_id = request.session['userinfo']['id']
    balance = Info.objects.get(id=u_id)
    money = balance.price
    if money >= t_price:
        money -= t_price
        balance.price = money
        balance.save()
        msg = json.dumps("")
        return HttpResponse(msg)
    else:
        msg = json.dumps("亲!你的余额不足额...")
        return HttpResponse(msg)


# 制作图片名
def picture_name(file_name):
    file_name_list = file_name.split('.')
    file_style = file_name_list[-1]
    return file_style


# 用户 信息页面以及头像上传
def change(request):
    if request.method == "GET":
        if hasattr(request, 'session') and 'userinfo' in request.session:
            try:
                u_id = request.session['userinfo']['id']
                user = Info.objects.get(id=u_id)
                return render(request, 'user/change.html', locals())
            except:
                return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/')
    elif request.method == "POST":
        # print('1')
        u_id = request.session['userinfo']['id']
        user_info = Info.objects.get(id=u_id)
        # print('2')
        u_img_fd = request.FILES["uimg"]
        file_style = picture_name(u_img_fd.name)
        change_name_m = '%s.%s' % (u_id, file_style)
        # print('3')
        change_name = os.path.join(settings.CHANGE_MEDIA_ROOT, change_name_m)
        try:
            with open(change_name, 'wb') as f:
                f.write(u_img_fd.file.read())
                user_info.head_img = change_name_m
                user_info.save()
                return HttpResponseRedirect('/')
        except:
            raise Http404
