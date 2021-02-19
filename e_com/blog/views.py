from django.shortcuts import render
from .models import Blogpost
# Create your views here.
from django.http import HttpResponse

def index(request):
    #return render(request, 'blog/index.html')
#change 5/8/19;2:49
    mypost = Blogpost.objects.all()
    return render(request, 'blog/index.html',{'myposts':mypost})

"""
def blogpost(request):
    return render(request, 'blog/blogpost.html')
"""
#change 1-8-19
def blogpost(request, id):
    post = Blogpost.objects.filter(post_id = id)[0]
    print(post)
    return render(request, 'blog/blogpost.html',
                  {'post':post})

