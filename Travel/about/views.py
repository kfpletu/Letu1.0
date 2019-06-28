from django.shortcuts import render

# Create your views here.

def about_views(request):
    return render(request,'about/about.html')

def travelContract_views(request):
    return render(request,'about/travelContract.html')

def childPrice_views(request):
    return render(request,'about/childPrice.html')

def touristRoute_views(request):
    return render(request,'about/touristRoute.html')

def singleRoom_views(request):
    return render(request,'about/singleRoom.html')

def travelInsuranceCategory_views(request):
    return render(request,'about/travelInsuranceCategory.html')