from django.shortcuts import render

# Create your views here.
from .models import *
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator


# 登录
def login(request):
    if request.method == 'GET':
        return render(request, 'user/login.html')
    elif request.method == 'POST':
        # 获取登录页面form表单提交的uname和upwd
        uname = request.POST.get('uname')
        upwd = request.POST.get('upwd')
        # 获取验证码
        validateCode = request.POST.get('validateCode')

        remember = request.POST.get('remember')
        # 从数据库获取uname和upwd
        try:
            user = Info.objects.get(uname=uname, upwd=upwd)
            if user.is_online:
                resp = render(request,'user/login.html',locals())
                return resp
            else:
                user.is_online = 1
                user.save()
                request.session['userinfo'] = {
                    'uname': user.uname,
                    'id': user.id
                }
                resp = render(request, 'index.html', locals())
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
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        # 获取数据库uname,判断是否重复
        if Info.objects.filter(uname=uname):
            return render(request, 'user/register.html', locals())
        else:
            try:
                newinfo = Info(uname=uname, upwd=upwd, phone=phone, email=email)
                newinfo.save()
                return render(request, 'index.html', locals())
            except:
                return render(request,'user/register.html',locals())

# 忘记密码
def getpwd(request):
    if request.method == 'GET':
        return render(request, 'user/forget.html')
    elif request.method == 'POST':

        # 获取用户输入的信息
        uname = request.POST.get('uname') # 用户名
        phone = request.POST.get('phone') # 电话号码
        email = request.POST.get('email') # 邮箱
        validateCode = request.POST.get('validateCode')  # 验证码

        try:
            info = Info.objects.get(uname=uname, phone=phone, email=email)
            request.session['uname'] = info.uname
            return render(request, 'user/forget_new.html')
        except:
            return render(request,'user/forget.html')
# 修改密码
def updatepwd(request):
    if request.method == 'GET':
        return render(request, 'user/forget.html')
    elif request.method == 'POST':
        # 获取用户输入的新密码
        uname = request.session['uname']
        new_pwd = request.POST.get('new_pwd')
        new_pwd_again = request.POST.get('new_pwd_again')
        if new_pwd == new_pwd_again:
            try:
                abook = Info.objects.get(uname=uname)
                abook.upwd = new_pwd
                abook.save()
                del request.session['uname']
                return render(request, 'user/login.html')
            except:
                return render(request, 'user/forget.html')
        else:
            pwd_error = '密码不一致'
            return render(request,'user/forget.html',locals())
        
# 退出登录
def logout(request):
    try:
        uid = request.session['userinfo']['id']
        user = Info.objects.get(id=uid)
        user.is_online = False
        user.save()
        # print(user.is_online)
        del request.session['userinfo']
        # del request.session['id']
        return HttpResponseRedirect('/')
    except:
        return HttpResponseRedirect('/')

    
def topup(request):
    return render(request, 'pay/topUp.html')

#订购成功跳转页面
def booking(request):
    return render(request,'user/booking.html',locals())
    

#购物车
def cart(request):
    # u_id = request.session[]['id']
    goods = Cart.objects.filter(user_id=69)
    paginator = Paginator(goods,4)
    print('啦啦啦啦',paginator.num_pages)
    # if paginator.num_pages > 3: 
    cur_page = request.GET.get('page',1)
    page = paginator.page(cur_page)
    return render(request,'user/cart.html',locals())

#历史记录
def order(request):
    return render(request, 'user/order.html')