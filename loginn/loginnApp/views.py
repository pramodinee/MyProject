# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse,HttpRequest

from django.shortcuts import render

# Create your views here.


def home(request):
    return HttpResponse('hello world')


def login(request):
    return HttpResponse('login')


def register(request):
    return HttpResponse('register')











