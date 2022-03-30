# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse,HttpRequest
from django.shortcuts import render
from loginnApp.models import employee


from django.shortcuts import render

# Create your views here.


def home(request):
    return HttpResponse('hello world')


def login(request):
    return HttpResponse('login')


def register(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        print('>>>>>>>>>>>>>>>>>>>>>>>name', name)
        print('>>>>>>>>>>>>>>>>>>>>>>>>>email',email)
        print('>>>>>>>>>>>>password',password)

        employee  (
         name = name,
         email = email,
         password = password
        ).save()
        return HttpResponse('Data save successfully')
    else:
        return render(request, 'register.html')












