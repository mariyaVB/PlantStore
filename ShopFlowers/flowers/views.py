from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from .models import Flowers, Category
from datetime import datetime
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView


class MainPage(TemplateView):
    template_name = 'main_page.html'


class FlowersView(ListView):
    model = Flowers
    template_name = 'flowers.html'
    context_object_name = 'flowers'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        flowers = Flowers.objects.all()
        context['categories'] = categories
        context['flowers'] = flowers

        return context


class FlowerDetailView(DetailView):
    model = Flowers
    template_name = 'flower.html'
    context_object_name = 'flower'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        flower = Flowers.objects.get(slug=self.kwargs['slug'])
        category = Category.objects.get(title=flower.category)
        context['category'] = category
        context['flower'] = flower

        return context


class CategoryView(ListView):
    model = Flowers
    template_name = 'flowers_category.html'
    context_object_name = 'flowers_category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        category = Category.objects.get(slug=self.kwargs['slug'])
        flowers = Flowers.objects.filter(category=category.id)
        context['category'] = category
        context['categories'] = categories
        context['flowers'] = flowers

        return context








