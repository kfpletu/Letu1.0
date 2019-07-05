from django.shortcuts import render


# Create your views here.


def index(request):
    uname = ''
    return render(request, 'index.html', locals())


def a404(request):
    return render(request, '404.html')
