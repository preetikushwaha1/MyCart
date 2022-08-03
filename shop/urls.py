from django.urls import path 
from shop import views

urlpatterns = [ 
        path("", views.index, name ="ShopHome"),
        path("about/", views.aboutUs, name="AboutUs"),
        path("contact/", views.contact, name="ContactUs"),
        path("tracker/", views.tracker, name="TrackingStatus"),
        path("search/", views.search, name="Search"),
        path("productview/<int:Myid>", views.productView, name="ProductView"),
        path("checkout/", views.checkout, name="CheckOut"),
]