from django.db.models import Q
from django.shortcuts import render
from django.http import Http404, JsonResponse
from django.urls import reverse_lazy

from .models import Flowers, Category
from django.views.generic import TemplateView, ListView, DetailView
from cart.models import Cart


# def error_404(request, exception):
#     return render(request, '404.html', status=404)


class MainPage(TemplateView):
    model = Cart
    context_object_name = 'carts'
    template_name = 'main_page.html'


class FlowersView(ListView):
    model = Flowers
    template_name = 'flowers.html'
    context_object_name = 'flowers'
    paginate_by = 12

    def get_category(self):
        return Category.objects.all()

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     try:
    #         categories = Category.objects.all()
    #         context['categories'] = categories
    #         return context
    #     except:
    #         raise Http404('Not Found')


class FilterFlowersView(FlowersView, ListView):
    def get_queryset(self):
        flowers = Flowers.objects.filter(category__in=self.request.GET.getlist('category.id'))
        return flowers


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








