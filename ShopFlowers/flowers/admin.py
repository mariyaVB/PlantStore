from django.contrib import admin
from .models import Flowers, Category

admin.site.index_title = 'Fresh Company'
admin.site.site_header = 'Управление Галереей зеленых пейзажей'


@admin.register(Flowers)
class FlowersAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text', 'image', 'quantity', 'price', 'category', 'slug', 'product')
    list_display_links = ('id', 'title')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug')
    list_display_links = ('id', 'title')

