from django.urls import path
from blog import views

urlpatterns = [
        path("", views.index, name="blogHome"),
        path("blogPost/", views.blogPost_fun, name="blogPost")

]