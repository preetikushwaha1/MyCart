
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, "shop/index.html")

#==========About Us ===========================#
def aboutUs(request):
    return HttpResponse("We at About Us page")


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