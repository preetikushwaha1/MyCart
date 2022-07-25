
from django.shortcuts import render
from django.http import HttpResponse
from shop.models import Product
from math import ceil


# Create your views here.
def index(request):
    Products = Product.objects.all()
    print(Products)
    n = len(Products)       # 6
    nSlide = n // 4 + ceil( (n/4)- (n//4))
    print(nSlide)
    params ={'no_of_slide':nSlide, 'range': range(nSlide), 'products': Products}
    return render(request, "shop/index.html", params)

#==========About Us ===========================#
def aboutUs(request):
    return render(request, "shop/about.html")


#============= Contact us =======================#

def contact(request):
    return HttpResponse("We are at Contact Us")

#========== Tracking Status  =====================#
def tracker(request):
    return HttpResponse("We are at Tracker page")

#============= Search ===========================#

def search(request):
    return HttpResponse("we are at searching page")

#============ Product View ======================#
def productView(request):
    return HttpResponse("We are at Product View")


#========== Check Out =====================#
def checkout(request):
    return HttpResponse("We are at Check Out page")