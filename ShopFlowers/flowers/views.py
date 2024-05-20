from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from .models import Flowers, Category
from datetime import datetime
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView


class MainPage(View):
    def get(self, request):
        return render(request, 'main_page.html')

    def post(self, request):
        pass


class FlowersView(ListView):
    model = Flowers
    template_name = 'flowers.html'
    context_object_name = 'flowers'

    def get_queryset(self):
        return Flowers.objects.all()


class FlowerDetailView(DetailView):
    model = Flowers
    template_name = 'flower.html'
    context_object_name = 'flower'
    slug_url_kwarg = 'slug'

    def get_queryset(self):
        return Flowers.objects.all()






