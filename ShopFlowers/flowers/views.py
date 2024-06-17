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
        flowers = Flowers.objects.filter(
            Q(category__in=self.request.GET.getlist('category')) |
            Q(price__in=self.request.GET.getlist('price'))
        )
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


# class JsonFilterFlowersView(ListView):
#     def get_queryset(self):
#         flowers = Flowers.objects.filter(
#             category__in=self.request.GET.getlist('category')).distinct().values(
#             'category_id', 'id', 'image', 'price', 'product', 'quantity', 'slug', 'text', 'title')
#         return flowers
#
#     def get(self, request, *args, **kwargs):
#         flowers_result = list(self.get_queryset())
#         return JsonResponse({'flowers': flowers_result}, safe=False)


def filter_flowers(request):
    # Получение данных из запроса
    category_id = request.GET.getlist('category')  # Получаем список выбранных категорий
    price = request.GET.get('price')
    # price_to = request.GET.get('price_to')

    # Фильтрация товаров
    flowers = Flowers.objects.filter(product='Комнатные растения')  # Фильтруем по типу продукта
    if category_id:
        flowers = flowers.filter(category__id__in=category_id)
    if price:
        flowers = flowers.filter(price__gte=price.min, price__lt=price.max)
    # if price_to:
    #     flowers = flowers.filter(price__lte=price_to)

    # Создание списка данных для JSON
    flower_data = [
        {
            "id": flower.id,
            "slug": flower.slug,
            "name": flower.title,
            "image": flower.image.url,
            "price": flower.price,
            "quantity": flower.quantity
        }
        for flower in flowers
    ]

    return JsonResponse(flower_data, safe=False)
