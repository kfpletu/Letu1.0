import hashlib
import json
import os
import random

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
from django.conf import settings
from django.core.paginator import Paginator
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from PIL import Image, ImageDraw, ImageFont

# 订单结算
from hotel.models import House

from .models import *


# 登录
def login(request):
    if request.method == 'GET':
        return render(request, 'user/login.html')
    elif request.method == 'POST':
        # 获取登录页面form表单提交的uname和upwd
        uname = request.POST.get('uname')
        upwd = request.POST.get('upwd')

        # 将密码进行hash
        s = 'letuTravel'
        h_p = hashlib.sha1()
        s_p = hashlib.sha1()
        h_p.update(upwd.encode())
        s_p.update(s.encode())
        upwd = h_p.hexdigest() + s_p.hexdigest()
        h_p = hashlib.sha1()
        h_p.update(upwd.encode())
        upwd = h_p.hexdigest()

        # 获取记住密码单选框的状态
        remember = request.POST.get('remember')
        try:
            # 从数据库获取uname和upwd
            user = Info.objects.get(uname=uname, upwd=upwd)
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
                    user.is_online = 1
                    user.save()
                    request.session['userinfo'] = {
                        'uname': user.uname,
                        'id': user.id
                    }

                    resp = HttpResponse('登录成功', locals())
                    if remember:
                        resp.set_cookie('uname', uname, max_age=7 * 24 * 60 * 60)
                    else:
                        resp.delete_cookie('uname')
                    return resp
        except:
            # 出异常,说明用户名密码不正确,刷新当前登录页面
            return HttpResponse('登录失败,请重新登录')


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

    font = ImageFont.truetype(
        "/usr/share/fonts/truetype/freefont/FreeSerif.ttf", 24)
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
        # 获取用户注册输入的信息
        uname = request.POST.get('uname')
        upwd = request.POST.get('upwd')

        # 将密码进行hash
        s = 'letuTravel'
        h_p = hashlib.sha1()
        s_p = hashlib.sha1()
        h_p.update(upwd.encode())
        s_p.update(s.encode())
        upwd = h_p.hexdigest() + s_p.hexdigest()
        h_p = hashlib.sha1()
        h_p.update(upwd.encode())
        upwd = h_p.hexdigest()

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

        # 将密码进行hash
        s = 'letuTravel'
        h_p = hashlib.sha1()
        s_p = hashlib.sha1()
        h_p.update(new_pwd.encode())
        s_p.update(s.encode())
        upwd = h_p.hexdigest() + s_p.hexdigest()
        h_p = hashlib.sha1()
        h_p.update(upwd.encode())
        upwd = h_p.hexdigest()

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
    u_id = request.session['userinfo']['id']
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
    uid = request.session['userinfo']['id']
    user = Info.objects.get(id=uid)
    datas = History_list.objects.filter(u_id=uid, is_del='1').order_by('-booking_time')
    paginator = Paginator(datas, 4)
    print(paginator.page_range)
    cur_page = request.GET.get('page', 1)
    page = paginator.page(cur_page)
    return render(request, 'user/order.html', locals())


# 删除购物车商品
def del_goods(request, g_id, num):
    target = Cart.objects.get(id=g_id)
    target.delete()
    u_id = request.session['userinfo']['id']
    goods = Cart.objects.filter(user_id=u_id, is_pay=0)
    paginator = Paginator(goods, 4)
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


def modif(request, g_id):
    target = Cart.objects.get(id=g_id)
    target.is_pay = 1
    target.save()
    try:
        house_id = int(str(target.g_img)[-8]) + int(str(target.g_img)[-10]) * 10
        # print(house_id)
        house = House.objects.get(id=house_id)
        house.order_count = house.order_count + 1
        house.save()
    except:
        pass
    finally:
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
        except:
            return HttpResponse('购买失败')
        else:

            return HttpResponse('payment.html')


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
    order = History_list.objects.filter(u_id=user_id, is_del=1)
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
