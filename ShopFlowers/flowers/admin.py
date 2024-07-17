from django.contrib import admin
from .models import Flowers, Category, Discount, News

admin.site.index_title = 'Fresh Company'
admin.site.site_header = 'Управление Галереей зеленых пейзажей'


@admin.register(Flowers)
class FlowersAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text', 'image', 'quantity', 'price', 'category', 'slug', 'product')
    list_display_links = ('id', 'title')
    list_filter = ['id', 'title', 'price', 'quantity', 'category', 'product']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug')
    list_display_links = ('id', 'title')


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'percent')
    list_display_links = ('id', 'title', 'percent')


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'link_image', 'link_new')
    list_display_links = ('id', 'text', 'link_image', 'link_new')
