from django.shortcuts import render
from django.views.generic import ListView
from flowers.models import Flowers
from feedback.models import Feedback, ImagesFeedback


class FeedbackProfileView(ListView):
    model = Feedback
    template_name = 'profile_feedback.html'
    context_object_name = 'feedbacks'
    paginate_by = 2

    def get_queryset(self):
        return Feedback.objects.filter(user=self.request.user)
