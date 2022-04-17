from django.conf.urls import url
from django.views.generic.base import RedirectView
from . import views
from django.urls import path, include
from django.contrib import admin



urlpatterns = [

    path('', RedirectView.as_view(url='/home', permanent=False), name='home'), #При загрузке сразу переходим на home
    path('home', views.home, name='home'),#Главная страница
    path('Profile', views.Profile, name='Profile'),


    ]