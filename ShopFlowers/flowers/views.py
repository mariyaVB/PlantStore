from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from .models import Flowers, Category
from datetime import datetime


def show_main_page(request):
    return render(request, 'main_page.html')


def show_flowers(request):
    flowers = Flowers.objects.all()
    data = {
        'flowers': flowers,
    }
    return render(request, 'flowers.html', context=data)


def qwerty(request):
    return render(request, '404.html', status=404)
