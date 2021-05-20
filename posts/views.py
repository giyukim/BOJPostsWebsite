from django.shortcuts import render

from .models import Post

def index(request):
    return render(request, 'index.html')

def posts(request):
    postlist = Post.objects.all
    return render(request, "posts.html", {"postlist":postlist})

def posting(request, pk):
    post = Post.objects.get(pk = pk)
    return render(request, "posting.html", {"post":post})