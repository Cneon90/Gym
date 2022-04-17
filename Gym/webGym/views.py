from django.shortcuts import render
from .models import *
from .function import *
from django.views.generic.base import TemplateView


# Create your views here.



def home(request):
    data = {}
    data = loadMenu(request)

    return render(request, 'webGym/index.html', data)


def Profile(request):
    data = {}
    data = loadMenu(request)
    return render(request, 'webGym/profile.html', data)
