from django.shortcuts import render,redirect
from django.contrib.auth.models import User

def articles(request):
    # To do
    return render(request,"blog/articles.html")

def detail_post(request):
    # To do
    return render(request,"blog/detail_post.html")

def contactezNous(request):
    # To do
    return render(request,"blog/contact.html")

