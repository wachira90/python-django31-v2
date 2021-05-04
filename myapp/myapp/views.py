#-*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render

from .forms import LoginForm

# def index(request):
#     text = "<h1>index !</h1>" 
#     return HttpResponse(text)

def index(request):
    return render(request, "hello.html", {})

def books(request, number):
    text = "<h1>welcome to my app number %s!</h1>"% number
    return HttpResponse(text)

def art(request, year):
    text = "<h1>art  %s </h1>"% year
    return HttpResponse(text)

def comment(request, id):
    text = "<h1>comment  %s </h1>"% id
    return HttpResponse(text)

def connection(request):
    if request.method == "GET":
        ttyy = 'test1234'
        return render(request, "login.html", {'ttyy':ttyy})

# def login(request):
#     return render(request, "login.html", {})

def hello(request):
    return render(request, "hello.html", {})

def test(request):
    text = "<h1>test !</h1>" 
    return HttpResponse(text)

def login(request):
    username = "not logged in"
    if request.method == "POST":
        #Get the posted form
        MyLoginForm = LoginForm(request.POST)
        if MyLoginForm.is_valid():
            username = MyLoginForm.cleaned_data['username']
    else:
        MyLoginForm = LoginForm()

    return render(request, 'loggedin.html', {"username" : username})