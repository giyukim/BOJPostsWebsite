from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from .forms import UserForm
from .models import Post

import datetime as dt

def index(request):
    return render(request, 'index.html')

def posts(request):
    postlist = Post.objects.all
    return render(request, "posts.html", {"postlist":postlist})

def posting(request, pk):
    post = Post.objects.get(pk = pk)
    return render(request, "posting.html", {"post":post})

def newpost(request):
    if request.method == "POST":
        new_article = Post.objects.create(
            title = request.POST["title"],
            plink = request.POST["plink"],
            code = request.POST["code"],
            content = request.POST["content"],
        )
        return redirect("/posts/")
    return render(request, "newpost.html")

def deletepost(request, pk):
    post = Post.objects.get(pk = pk)
    if request.method == 'POST':
        post.delete()
        return redirect("/posts/")
    return render(request, 'deletepost.html', {'Post': post})

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username = username, password = raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserForm()
    return render(request, 'signup.html', {'form': form})