from django.shortcuts import render

# Create your views here.
# Create your views here.
def index(request):
    if request.method=='GET':
        return render(request,'scenic/information.html')
def ticket(request):
    if request.method == 'GET':
        return render(request,'scenic/ticket.html')
def scenic2(request):
    if request.method == 'GET':
        return render(request,'scenic/information02.html')