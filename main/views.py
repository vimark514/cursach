from django.http import HttpResponse
from django.shortcuts import render
from django.template import context
from django.template.defaulttags import lorem

from goods.models import Categories

# Create your views here.
def index(request):

    context = {
        'title': 'BMW - Main',
        'content': 'Find your BMW',
    }

    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'Home - About',
    }

    return render(request, 'main/about.html', context)