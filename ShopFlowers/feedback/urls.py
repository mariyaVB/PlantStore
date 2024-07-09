from django.urls import path, reverse_lazy
import feedback.views as feedback

app_name = 'feedback'
urlpatterns = [
    path('feedback_profile/', feedback.FeedbackProfileView.as_view(), name='feedback-profile'),
    path('add_feedback/<int:product_id>/', feedback.AddFeedbackView.as_view(), name='add-feedback'),
    path('edit_feedback/<int:feedback_id>/', feedback.EditFeedbackView.as_view(), name='edit-feedback'),
    path('remove_feedback/<int:feedback_id>/', feedback.RemoveFeedbackView.as_view(), name='remove-feedback'),
]
