from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def venky1(request):
    return HttpResponse('app1 of venky1')

def venky2(request):
    return HttpResponse('app1 of venky2')