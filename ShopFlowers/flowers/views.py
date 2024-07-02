import random
from django.db.models import Q
from django.http import Http404, JsonResponse
from .models import Flowers, Category
from django.views.generic import TemplateView, ListView, DetailView
from cart.models import Cart
from feedback.models import Feedback


class MainPage(TemplateView):
    model = Cart
    context_object_name = 'carts'
    template_name = 'main_page.html'


class FlowersView(ListView):
    """Показ комнатных растений"""
    model = Flowers
    queryset = Flowers.objects.filter(product='Комнатные растения')
    template_name = 'flowers.html'
    context_object_name = 'flowers'
    paginate_by = 12

    def get_category(self):
        return Category.objects.all()


class PotsView(ListView):
    """Показ горшков для растений"""
    model = Flowers
    queryset = Flowers.objects.filter(product='Горшки')
    template_name = 'pots.html'
    context_object_name = 'pots'
    paginate_by = 12

    def get_category(self):
        return Category.objects.all()


class CareView(ListView):
    """Показ ухода для растений"""
    model = Flowers
    queryset = Flowers.objects.filter(product='Уход')
    template_name = 'care.html'
    context_object_name = 'cares'
    paginate_by = 12

    def get_category(self):
        return Category.objects.all()


class FlowerDetailView(DetailView):
    """Показ товаров детально"""
    model = Flowers
    template_name = 'flower.html'
    context_object_name = 'flower'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        flower = Flowers.objects.get(slug=self.kwargs['slug'])
        assortments = Flowers.objects.all()
        random_assortments = random.sample(list(assortments), len(assortments))
        category = Category.objects.get(title=flower.category)
        feedbacks = Feedback.objects.filter(flowers=flower.id)
        context['category'] = category
        context['flower'] = flower
        context['assortments'] = random_assortments
        context['feedbacks'] = feedbacks

        return context


class CategoryView(ListView):
    """Показ категорий товаров"""
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


class Search(ListView):
    """Поиск товаров на сайте"""
    paginate_by = 12
    template_name = 'flowers_search.html'

    def get_queryset(self):
        return Flowers.objects.filter(
            Q(title__icontains=self.request.GET.get('search')) |
            Q(category__title__icontains=self.request.GET.get('search'))
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title = self.request.GET.get('search')
        context['title'] = title
        context['search'] = Flowers.objects.filter(
            Q(title__icontains=self.request.GET.get('search')) |
            Q(category__title__icontains=self.request.GET.get('search'))
        )
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
#
# class FilterFlowersView(FlowersView, ListView):
#     def get_queryset(self):
#         flowers = Flowers.objects.filter(
#             Q(category__in=self.request.GET.getlist('category')) |
#             Q(price__in=self.request.GET.getlist('price'))
#         )
#         return flowers