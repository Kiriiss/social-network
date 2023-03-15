from django.contrib import admin
from django.urls import path, include
from network.views import home

app_name = 'network'

urlpatterns = [
    path('', home, name='home'),
]
