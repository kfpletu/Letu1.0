from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
from django.shortcuts import render, redirect
import json

# Create your views here.
from .models import *
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from .page_helper import *
from django.contrib.auth.hashers import make_password, check_password


# 登录
def login(request):
    if request.method == 'GET':
        return render(request, 'user/login.html')
    elif request.method == 'POST':
        # 获取登录页面form表单提交的uname和upwd
        uname = request.POST.get('uname')
        upwd = request.POST.get('upwd')
        upwd = make_password(upwd, 'xiaochen', 'pbkdf2_sha256')
        # 获取验证码
        validateCode = request.POST.get('validateCode')
        print(validateCode)
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


# 验证码


def yanzma(request):
    """
        登录图形图形验证码
    """
    img = Image.new("RGB", (110, 37), (255, 255, 255))
    code = [chr(x) for x in range(97, 123)] + [str(x) for x in range(10)]
    code = random.sample(code, 6)
    code = ''.join(code)
    draw = ImageDraw.Draw(img)
    for _ in range(10):
        draw.point(
            (random.randint(0, 150), random.randint(0, 50)),  # 坐标
            fill=(0, 0, 0))  # 颜色
    for _ in range(10):
        draw.line([(random.randint(0, 150), random.randint(0, 50)),
                   (random.randint(0, 150), random.randint(0, 50))],
                  fill=(150, 150, 2))

    font = ImageFont.truetype(
        "/usr/share/fonts/truetype/freefont/FreeSerif.ttf", 24)
    draw.text((30, 10), code, font=font, fill="green")
    src = 'static/images/logImg/code.jpg'
    img.save(src)
    src = '/static/images/logImg/code.jpg'
    imgUrl = {
        'url': src,
        'code': code
    }
    return HttpResponse(json.dumps(imgUrl))


# 注册
def register(request):
    if request.method == 'GET':
        return render(request, 'user/register.html')
    elif request.method == 'POST':
        # 获取用户注册输入的信息
        uname = request.POST.get('uname')
        upwd = request.POST.get('upwd')
        upwd = make_password(upwd, 'xiaochen', 'pbkdf2_sha256')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        # 尝试向数据库添加用户信息,成功返回到登录页面进行登录
        try:
            Info.objects.create(uname=uname, upwd=upwd, phone=phone, email=email)
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


# 忘记密码
def getpwd(request):
    if request.method == 'GET':
        return render(request, 'user/forget.html')
    elif request.method == 'POST':

        # 获取用户输入的信息
        uname = request.POST.get('uname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        validateCode = request.POST.get('validateCode')

        # 将用户输入的信息与数据库进行比对,正确则发送seesion,返回重置密码页面
        try:
            info = Info.objects.get(uname=uname, phone=phone, email=email)
            request.session['uname'] = info.uname
            return render(request, 'user/forget_new.html')
        except:
            # 抛异常则输入信息不正确,刷新忘记密码页面
            return render(request, 'user/forget.html')


# 修改密码
def updatepwd(request):
    if request.method == 'GET':
        return render(request, 'user/forget.html')
    elif request.method == 'POST':
        # 获取用户输入的新密码
        uname = request.session['uname']
        new_pwd = request.POST.get('new_pwd')
        new_pwd = make_password(new_pwd, 'xiaochen', 'pbkdf2_sha256')
        new_pwd_again = request.POST.get('new_pwd_again')
        new_pwd_again = make_password(new_pwd_again, 'xiaochen', 'pbkdf2_sha256')
        # 判断两次密码是否一致
        if new_pwd == new_pwd_again:
            try:
                # 修改相应用户的密码,删除seesion,返回登录页面
                abook = Info.objects.get(uname=uname)
                abook.upwd = new_pwd
                abook.save()
                del request.session['uname']
                return HttpResponseRedirect('/user/login')
            except:
                # 重新返回忘记密码页面
                return render(request, 'user/forget.html')
        else:
            # 如果两次密码不一致,刷新忘记密码页面,返回错误信息
            pwd_error = '密码不一致'
            return render(request, 'user/forget_new.html', locals())


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
        return HttpResponseRedirect('/')
    except:
        # 直接返回首页,但不删除seesion
        return HttpResponseRedirect('/')


# 订购成功跳转页面
def booking(request):
    return render(request, 'user/booking.html', locals())


# 购物车
def cart(request):
    u_id = request.session['userinfo']['id']
    balance = Info.objects.get(id=u_id)
    goods = Cart.objects.filter(user_id=u_id, is_pay=0)
    paginator = Paginator(goods, 4)
    cur_page = request.GET.get('page', 1)
    page = paginator.page(cur_page)
    return render(request, 'user/cart.html', locals())


# 历史记录
def order(request):
    uid = request.session['userinfo']['id']
    data = History_list.objects.filter(u_id=uid, is_del='1').all()
    if data:
        return render(request, 'user/order.html', locals())
    return render(request, 'user/order.html', locals())


# 删除购物车商品
def del_goods(request, g_id):
    target = Cart.objects.get(id=g_id)
    target.delete()
    return render(request, 'user/cart.html')


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


# 订单结算
def modif(request, g_id):
    target = Cart.objects.get(id=g_id)
    target.is_pay = 1
    target.save()
    try:
        a_order = History_list.objects.create(
            u_id=target.user_id,
            g_img=target.g_img,
            g_name=target.g_name,
            time1=target.time1,
            time2=target.time2,
            g_type=target.g_type,
            price=target.price,
            g_num=target.g_num,
            total_price=target.total_price,
            booking_time='2019-2-2',
            is_del=target.is_pay
        )
    except:
        return HttpResponse('购买失败')
    # else:
    #     return render(request,'user/payment.html')


def payment(request):
    return render(request, 'user/payment.html')


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
    充值功能的实现
    成功:返回True 1
    失败:返回False 0
    :param request:
    :return: 布尔值,前端进行判断使用
    """
    if request.method == "GET":
        return render(request, 'pay/topUp.html')
    elif request.method == "POST":
        uid = request.session['userinfo']['id']
        money = float(request.POST['money'])
        money1 = float(request.POST['money1'])
        try:
            user = Info.objects.get(id=uid)
            if money == 0 and money1 != 0:
                change_money = float(user.price)
                change_money = change_money + money1
            elif money1 == 0 and money != 0:
                change_money = float(user.price)
                change_money = change_money + money
            user.price = change_money
            user.save()
            return HttpResponse("1")
        except:
            return HttpResponse("0")


def delete(request):
    """
    用户删除自己的购买记录
    :param request: 前端的请求
    :return:
    """
    id = request.GET['id']
    data = History_list.objects.filter(id=id)
    data.update(is_del=0)
    return redirect('/user/order')
    # return render(request,'user/order.html')


# 余额
def balance(request):
    t_price = request.GET["totalPrice"]
    t_price = int(t_price)
    u_id = request.session['userinfo']['id']
    balance = Info.objects.get(id=u_id)
    money = balance.price
    if money > t_price:
        money -= t_price
        balance.price = money
        balance.save()
        return render(request, 'user/payment.html')
    else:
        print('嘎嘎嘎嘎嘎嘎个', money)
        msg = json.dumps("亲!你的余额不足额")
        return HttpResponse(msg)
