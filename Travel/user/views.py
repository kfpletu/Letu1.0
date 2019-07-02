from django.shortcuts import render

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
        # 获取记住密码单选框的状态
        remember = request.POST.get('remember')
        try:
            # 从数据库获取uname和upwd
            user = Info.objects.get(uname=uname, upwd=upwd)
            # 登录状态为真,刷新登录页面,禁止登录
            if user.is_alive:
                resp = render(request, 'user/login.html', locals())
                return resp
            else:
                if user.is_online:
                    resp = render(request,'user/login.html',locals())
                    return resp
                else:
                    # 修改登录状态,发送seesion,cookie,返回首页
                    user.is_online = 1
                    user.save()
                    request.session['userinfo'] = {
                        'uname': user.uname,
                        'id': user.id
                    }
                    resp = HttpResponseRedirect('/', locals())
                    if remember:
                        resp.set_cookie('uname', uname, max_age=7 * 24 * 60 * 60)
                    else:
                        resp.delete_cookie('uname')
                    return resp
        except:
            # 出异常,说明用户名密码不正确,刷新当前登录页面
            return render(request,'user/login.html')

#注册
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
        # 获取数据库uname,判断是否重复
        if Info.objects.filter(uname=uname):
            return render(request, 'user/register.html', locals())
        else:
            # 尝试向数据库添加用户信息,成功返回到登录页面进行登录
            try:
                newinfo = Info(uname=uname, upwd=upwd, phone=phone, email=email)
                newinfo.save()
                return render(request, 'user/login.html', locals())
            except:
                # 抛异常,刷新注册页面,重新注册
                return render(request,'user/register.html',locals())

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
            # 抛异常ze输入信息不正确,刷新忘记密码页面
            return render(request,'user/forget.html')
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
                return render(request, 'user/login.html')
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

    
def topup(request):
    return render(request, 'pay/topUp.html')

#订购成功跳转页面
def booking(request):
    return render(request,'user/booking.html',locals())
    

#购物车
def cart(request):
    u_id = request.session['userinfo']['id']
    goods = Cart.objects.filter(user_id=u_id)
    paginator = Paginator(goods,4) 
    cur_page = request.GET.get('page',1)
    page = paginator.page(cur_page)
    return render(request,'user/cart.html',locals())

#历史记录
def order(request):
    uid=request.session['userinfo']['id']
    # page_num=request.GET.get('page')
    # data=History_list.objects.filter(u_id=uid)
    # data_counts=data.count()
    # page_obj=Page(page_num,data_counts,url_prefix="/user/order/",per_page=4,max_page=6)
    # all_data_order=History_list.objects.filter(u_id=uid)[page_obj.start:page_obj.end]
    # page_html=page_obj.page_html()
    data=History_list.objects.filter(u_id=uid).all()
    if data:
        return render(request, 'user/order.html',locals())
    return render(request, 'user/order.html')

#删除购物车商品
def del_goods(request,g_id):
    target = Cart.objects.get(id=g_id)
    target.delete()
    return render(request,'user/cart.html')


def add(request,g_id):
    target = Cart.objects.get(id=g_id)
    p = target.g_num
    p += 1
    target.g_num = p
    # target.save()
    print("啦啦啦",target.g_num)
    return render(request,'user/cart.html')
    
def payment(request):
    print("哈哈哈")
    return render(request,'user/payment.html')