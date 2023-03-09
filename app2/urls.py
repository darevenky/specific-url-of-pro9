from django.urls import path
from app2.views import *

app_name='none'

urlpatterns=[
    path('venkydare1/',venkydare1,name='venkydare1'),
    path('venkydare2/',venkydare2,name='venkydare2'),
]