from django.contrib import admin
from .models import Flowers, Category

admin.site.index_title = 'Greenscape Gallery'
admin.site.site_header = 'Управление Greenscape Gallery'


@admin.register(Flowers)
class FlowersAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text', 'image', 'price', 'category', 'slug')
    list_display_links = ('id', 'title')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug')
    list_display_links = ('id', 'title')

