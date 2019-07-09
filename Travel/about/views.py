from django.http import Http404
from django.shortcuts import render

# Create your views here.
from user.models import Info


def about_views(request):
    try:
        if hasattr(request, 'session') and 'userinfo' in request.session:
            uid = request.session['userinfo']['id']
            user = Info.objects.get(id=uid)
    except:
        raise Http404
    return render(request, 'about/about.html', locals())


def travelContract_views(request):
    try:
        if hasattr(request, 'session') and 'userinfo' in request.session:
            uid = request.session['userinfo']['id']
            user = Info.objects.get(id=uid)
    except:
        raise Http404
    return render(request, 'about/travelContract.html', locals())


def childPrice_views(request):
    try:
        if hasattr(request, 'session') and 'userinfo' in request.session:
            uid = request.session['userinfo']['id']
            user = Info.objects.get(id=uid)
    except:
        raise Http404
    return render(request, 'about/childPrice.html', locals())


def touristRoute_views(request):
    try:
        if hasattr(request, 'session') and 'userinfo' in request.session:
            uid = request.session['userinfo']['id']
            user = Info.objects.get(id=uid)
    except:
        raise Http404
    return render(request, 'about/touristRoute.html', locals())


def singleRoom_views(request):
    try:
        if hasattr(request, 'session') and 'userinfo' in request.session:
            uid = request.session['userinfo']['id']
            user = Info.objects.get(id=uid)
    except:
        raise Http404
    return render(request, 'about/singleRoom.html', locals())


def travelInsuranceCategory_views(request):
    try:
        if hasattr(request, 'session') and 'userinfo' in request.session:
            uid = request.session['userinfo']['id']
            user = Info.objects.get(id=uid)
    except:
        raise Http404
    return render(request, 'about/travelInsuranceCategory.html', locals())
