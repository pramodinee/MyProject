# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request,'home.html')

def register(request):
    return render(request,'register.html')

def login(request):
    return render(request,'login.html')

def logout(request):
    return render(request,'logout.html')

def forgotPassword(request):
    return render(request,'forgotPassword.html')



