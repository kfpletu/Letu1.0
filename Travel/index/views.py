from django.shortcuts import render
from user import models

# Create your views here.


def index(request):
    uname = ''
    try:
        if hasattr(request,'session') and 'userinfo' in request.session:
            u_id = request.session['userinfo']['id']
            user=models.Info.objects.get(id=u_id)
        return render(request, 'index.html', locals())
    except:
        return render(request, 'index.html', locals())


def a404(request):
    return render(request, '404.html')
