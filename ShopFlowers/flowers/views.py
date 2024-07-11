import random
from django.core.paginator import Paginator
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
    template_name = 'flowers.html'
    context_object_name = 'flowers'
    paginate_by = 12

    def get_queryset(self):
        return Flowers.objects.filter(product='Комнатные растения').order_by('title')

    """Категории товаров для фильтрации"""
    def get_category(self):
        return Category.objects.all()


class PotsView(ListView):
    """Показ горшков для растений"""
    model = Flowers
    template_name = 'pots.html'
    context_object_name = 'pots'
    paginate_by = 12

    def get_queryset(self):
        return Flowers.objects.filter(product='Горшки').order_by('title')

    def get_category(self):
        return Category.objects.all()


class CareView(ListView):
    """Показ ухода для растений"""
    model = Flowers
    template_name = 'care.html'
    context_object_name = 'cares'
    paginate_by = 12

    def get_queryset(self):
        return Flowers.objects.filter(product='Уход').order_by('title')

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


class FilterFlowersView(FlowersView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        price = self.request.GET.getlist('price')
        product = self.request.GET.getlist('product')
        category = self.request.GET.getlist('category')
        price_filter = Q()
        if 'extra-price' in price:
            price_filter |= Q(price__lte=1000, product__in=product)
        elif 'rare-price' in price:
            price_filter |= Q(price__gt=1000, price__lte=5000, product__in=product)
        elif 'medium-price' in price:
            price_filter |= Q(price__gt=5000, price__lte=10000, product__in=product)
        elif 'well-done-price' in price:
            price_filter |= Q(price__gt=10000, product__in=product)
        else:
            pass
        product_category_filter = Q(product__in=product) & Q(category__in=category)

        if price and product and category:
            flowers = Flowers.objects.filter(price_filter & product_category_filter)
        elif price:
            flowers = Flowers.objects.filter(price_filter)
        elif category:
            flowers = Flowers.objects.filter(product_category_filter)
        else:
            pass

        paginator = Paginator(flowers, 12)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['flowers'] = flowers
        context['paginator'] = page_obj
        return context


class FilterCaresView(CareView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        price = self.request.GET.getlist('price')
        product = self.request.GET.getlist('product')
        category = self.request.GET.getlist('category')
        price_filter = Q()
        if 'extra-price' in price:
            price_filter |= Q(price__lte=1000, product__in=product)
        elif 'rare-price' in price:
            price_filter |= Q(price__gt=1000, price__lte=5000, product__in=product)
        elif 'medium-price' in price:
            price_filter |= Q(price__gt=5000, price__lte=10000, product__in=product)
        elif 'well-done-price' in price:
            price_filter |= Q(price__gt=10000, product__in=product)
        else:
            pass
        product_category_filter = Q(product__in=product) & Q(category__in=category)

        if price and product and category:
            cares = Flowers.objects.filter(price_filter & product_category_filter)
        elif price:
            cares = Flowers.objects.filter(price_filter)
        elif category:
            cares = Flowers.objects.filter(product_category_filter)
        else:
            pass

        paginator = Paginator(cares, 12)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['cares'] = cares
        context['paginator'] = page_obj
        return context


class FilterPotsView(PotsView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        price = self.request.GET.getlist('price')
        product = self.request.GET.getlist('product')
        category = self.request.GET.getlist('category')
        price_filter = Q()
        if 'extra-price' in price:
            price_filter |= Q(price__lte=1000, product__in=product)
        elif 'rare-price' in price:
            price_filter |= Q(price__gt=1000, price__lte=5000, product__in=product)
        elif 'medium-price' in price:
            price_filter |= Q(price__gt=5000, price__lte=10000, product__in=product)
        elif 'well-done-price' in price:
            price_filter |= Q(price__gt=10000, product__in=product)
        else:
            pass
        product_category_filter = Q(product__in=product) & Q(category__in=category)

        if price and product and category:
            pots = Flowers.objects.filter(price_filter & product_category_filter)
        elif price:
            pots = Flowers.objects.filter(price_filter)
        elif category:
            pots = Flowers.objects.filter(product_category_filter)
        else:
            pass

        paginator = Paginator(pots, 12)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['pots'] = pots
        context['paginator'] = page_obj
        return context

