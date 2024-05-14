from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from .models import Flowers, Category
from datetime import datetime


def show_flowers(request):
    flowers = Flowers.objects.all()
    data = {
        'flowers': flowers,
    }
    return render(request, 'flowers.html', context=data)
