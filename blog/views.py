from django.shortcuts import render
from django.http import HttpResponse
from .models import BlogPost
# Create your views here.

def index(request):
    mypost = BlogPost.objects.all()
    print(mypost)
    return render(request, "blog/index.html", {'mypost':mypost})



def blogPost_fun(request, id):

    post = BlogPost.objects.filter(post_id = id)[0]       # fetch data from data base
    #print(post)

    return render(request, "blog/blog_post.html", {'post':post})
