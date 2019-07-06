from django.shortcuts import render
from user import models

# Create your views here.


def index(request):
    uname = ''
    if hasattr request.session and request.session['userinfo']['id']:
        u_id = request.session['userinfo']['id']
        head_img=models.Info.objects.head_img
    return render(request, 'index.html', locals())


def a404(request):
    return render(request, '404.html')
