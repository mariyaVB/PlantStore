from django.contrib import admin
from feedback.models import Feedback, ImagesFeedback


@admin.register(ImagesFeedback)
class ImagesFeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'image1', 'image2', 'image3')
    list_display_links = ('id', 'image1', 'image2', 'image3')
    list_filter = ['id']


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'flowers', 'rating', 'text', 'images_feedback', 'date_created', 'date_updated')
    list_display_links = ('id', 'flowers')
    list_filter = ['id', 'rating']
