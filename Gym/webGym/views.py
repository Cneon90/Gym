import os
import random
from pathlib import Path

from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.template import context
from django import forms
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import *
from django.core.exceptions import ValidationError

from .models import *
from .forms import *
from .function import *
from django.views.generic.base import TemplateView
from django.views.generic import TemplateView, ListView, CreateView
import json


# Create your views here.


BASE_DIR = Path(__file__).resolve().parent.parent
def home(request):
    data = {}
    data = loadMenu(request)

    return render(request, 'webGym/index.html', data)


class AboutView(ListView):
    template_name = "webGym/index.html"
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = "kirill"
        return context
    def get_queryset(self):
        return 1

# class registration(ListView):
#     template_name = "webGym/reg.html"
#     context_object_name = 'posts'
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['menu'] = "kirill"
#         return context
#     def get_queryset(self):
#         return 1

# class auth(ListView):
#     template_name = "webGym/auth.html"
#     context_object_name = 'posts'
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['menu'] = "kirill"
#         return context
#     def get_queryset(self):
#         return 1

def Profile(request):
        data = {}
        data = loadMenu(request)
        return render(request, 'webGym/profile.html', data)



class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'webGym/reg.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = "kirill"
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'webGym/auth.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = "kirill"
        return context

    def get_success_url(self):
        return reverse_lazy('home')


class MyCabinet(ListView):
    template_name = 'webGym/my.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        names = ("bob", "dan", "jack", "lizzy", "susan")

        items = []
        for i in range(10):
            items.append({
                "name": random.choice(names),
                "age": random.randint(20, 80),
                "url": "https://example.com",
            })

        context = {}
        context["items"] = items
        context["items_json"] = json.dumps(items)
        return context
    def get_queryset(self):
        return 1



def logout_user(request):
    logout(request)
    return redirect('home')
