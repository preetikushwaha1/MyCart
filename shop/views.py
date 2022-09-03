
from sre_constants import SUCCESS
from warnings import catch_warnings
from django.shortcuts import render
from django.http import HttpResponse
from shop.models import Order_update, Product, Contact, Orders
from math import ceil

import json


# Create your views here.
def index(request):
    #Products = Product.objects.all()
    #print(Products)
   # n = len(Products)       # 6
    #nSlide = n // 4 + ceil( (n/4)- (n//4))  #6//4 + ceil((6/4)-(6//4)) = 0+ ceil(2 - 0) = 2
    #print(nSlide)"""

    all_prods =[]
    category_prods = Product.objects.values('id', 'category')
    print(category_prods)
    categories = { item['category'] for item in category_prods}
    for cat in categories:
        prods = Product.objects.filter(category = cat)
        n= len(prods)            #6
        nSlide = n//4 + ceil((n/4)- (n//4))    
        print("nSlide=",nSlide) 
        all_prods.append([prods, range(1, nSlide), nSlide])
        print(cat)

    #params ={'no_of_slide':nSlide, 'range': range(1,nSlide), 'products': Products}  #list 1

    #==== Now will create a list of list ---======================#
    """all_prods = [ [Products, range(1, nSlide), nSlide ],
                    [Products, range(1, nSlide), nSlide ] ] """
    return render(request, "shop/index.html", {'all_prods': all_prods})

#==========About Us ===========================#
def aboutUs(request):
    return render(request, "shop/about.html")


#============= Contact us =======================#

def contact(request):

    if request.method == "POST":
        #print("request preeti",request)
        name = request.POST.get('name'," ")
        email = request.POST.get('email'," ")
        phone = request.POST.get('phone'," ")
        desc = request.POST.get('desc'," ")

        #print(name,email,phone,desc)
        contact_obj = Contact(con_name=name, con_email=email,con_phone=phone,con_desc=desc)  #sending data into database
        contact_obj.save()

        success = True
        return render(request, "shop/contact.html", {'success':success})

    return render(request, "shop/contact.html")



#========== Tracking Status  =====================#
def tracker(request):

    if request.method == "POST":
        orderId = request.POST.get('orderId', "")
        email = request.POST.get('email',"")
        #return HttpResponse(f"{orderId} and {email}")
        try:
            order = Orders.objects.filter(order_id= orderId, ord_email = email)
            if(len(order)>0):
                update = Order_update.objects.filter(order_id=orderId)
                updates =[]
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps(updates, default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')

        except Exception as e:
            return HttpResponse('{}')
            #return HttpResponse(f"exception{e}")  #to print the exception on console log
    return render(request, "shop/tracker.html")


#============= Search ===========================#

def search(request):
    return HttpResponse("we are at searching page")

#============ Product View ======================#
def productView(request, Myid):
    #fetch the product using the id
    
    product = Product.objects.filter(id = Myid)
    return render(request, "shop/prodView.html" , {'access_prod' : product[0]})


#========== Check Out =====================#
def checkout(request):
    if request.method =="POST":
        item_json = request.POST.get('itemsJson'," ")
        name= request.POST.get('inputname'," ")
        email = request.POST.get('inputEmail4'," ")
        phone_no = request.POST.get('inputPhone'," ")
        Address = request.POST.get('inputAddress'," ") + " " +request.POST.get('inputAddress2'," ")
        City = request.POST.get('inputCity'," ")
        State = request.POST.get('inputState'," ")
        Zip_code = request.POST.get('inputZip'," ")

        Orders_obj = Orders(items_json=item_json,ord_name=name, ord_email=email, ord_phone_no=phone_no, ord_Address=Address, ord_city=City,
                        ord_state=State, ord_zip_code=Zip_code)  #stores data in database
        Orders_obj.save()   

        order_update = Order_update(order_id=Orders_obj.order_id, update_desc = "The order has been placed")
        order_update.save()

        success= True
        id = Orders_obj.order_id
        return render(request, "shop/checkout.html",{'success':success, 'id':id})

    return render(request, "shop/checkout.html")