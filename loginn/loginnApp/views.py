# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse,HttpRequest
from django.shortcuts import render
from loginnApp.models import employee


from django.shortcuts import render,redirect
from django.contrib.auth import authenticate

# Create your views here.


def home(request):
    return HttpResponse('welcome to home')


def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user:
            print('uuuuuuuuuuu',user)
            return redirect(home)
        else:
            return redirect(login)
    else:
        return render(request, 'login.html')


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
        return redirect(login)
    else:
        return render(request, 'register.html')












