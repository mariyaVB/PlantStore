from django.contrib import admin
from feedback.models import Feedback


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'flowers', 'rating', 'text', 'date_created', 'date_updated')
    list_display_links = ('id', 'flowers', 'date_created', 'date_updated')
    list_filter = ['id', 'rating', 'date_created', 'date_updated']
