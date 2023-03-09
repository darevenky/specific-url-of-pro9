from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def venkydare1(request):
    return HttpResponse('app2 of venkydare1')

def venkydare2(request):
    return HttpResponse('app2 of venkydare2')