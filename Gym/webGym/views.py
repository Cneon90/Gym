from django.shortcuts import render
from django.template import context

from .models import *
from .function import *
from django.views.generic.base import TemplateView
from django.views.generic import TemplateView, ListView


# Create your views here.



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

def Profile(request):
    data = {}
    data = loadMenu(request)
    return render(request, 'webGym/profile.html', data)


def as_view():
    pass

