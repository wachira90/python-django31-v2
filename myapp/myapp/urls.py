#-*- coding: utf-8 -*-
"""myapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path

from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('', views.index, ),
    path('admin/', admin.site.urls),

    path('connection/', views.connection ),

    path('login/', views.login),

    # path('login/', TemplateView.as_view(template_name='login.html')),

    #http://localhost:8000/books/11299
    path('books/<int:number>/', views.books),

    #http://localhost:8000/art/2020/
    re_path(r'^art/(?P<year>[0-9]{4})/$', views.art),

    #http://localhost:8000/comment/page-1984/
    re_path(r'^comment/(?:page-(?P<id>\d+)/)?$', views.comment),

    path('test/', views.test, name='test'),

    path('hello/', views.hello, name='hello'),
]
