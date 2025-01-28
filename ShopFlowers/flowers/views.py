import random
from django.http import Http404
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import schedule
from django.views.generic import ListView, DetailView, TemplateView
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Flowers, Category, News
from feedback.models import Feedback


class MainPage(TemplateView):
    """Стартовая страница"""
    def plant_news(self, request):
        chrome_options = Options()
        chrome_options.add_argument('headless')
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://plants-flowers.ru/")

        html_doc = driver.page_source
        soup = BeautifulSoup(html_doc, 'lxml')
        find_img = soup.find_all('div', class_='ast-blog-featured-section post-thumb ast-width-md-6')[:3]
        find_text_link = soup.find_all('h2', class_='entry-title')[:3]

        news = News.objects.all()
        if news:
            for new in news:
                new.delete()
        else:
            for text_link, img in zip(find_text_link, find_img):
                title = text_link.get_text(strip=True)
                link = text_link.find('a')['href']
                images = img.find('img', class_='attachment-400x400 size-400x400')['src']
                News.objects.create(link_image=images, link_new=link, text=title)

            driver.quit()

    schedule.every().sunday.at('06:00').do(plant_news)

    template_name = 'main_page.html'
    extra_context = {
        'title': 'Галерея зеленых пейзажей Fresh Company',
        'plants_news': News.objects.all(),
        'favorites': set(Feedback.objects.filter(Q(rating__gte=4, rating__lte=5))),
    }


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
        try:
            flower = Flowers.objects.get(slug=self.kwargs['slug'])
            category = Category.objects.get(title=flower.category)
            feedbacks = Feedback.objects.filter(flowers=flower.id)
        except (Feedback.DoesNotExist, Category.DoesNotExist, Flowers.DoesNotExist):
            return Http404('Объект Цветов, Категории или отзывов не найден')

        assortments = Flowers.objects.all()
        random_assortments = random.sample(list(assortments), len(assortments))
        context['category'] = category
        context['flower'] = flower
        context['assortments'] = random_assortments
        context['feedbacks'] = feedbacks

        return context


class Search(ListView):
    """Поиск товаров на сайте"""
    model = Flowers
    template_name = 'flowers_search.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title = self.request.GET.get('search')
        context['title'] = title
        context['search'] = Flowers.objects.filter(
            Q(title__icontains=title) |
            Q(category__title__icontains=title)
        )
        return context


class FilterFlowersView(FlowersView):
    """Фильтрация растений"""
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
    """Фильтрация ухода"""
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
    """Фильтрация горшков"""
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

