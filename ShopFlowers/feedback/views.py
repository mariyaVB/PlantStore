from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic import ListView,  UpdateView
from flowers.models import Flowers
from cart.models import Cart
from feedback.models import Feedback
from feedback.forms import AddFeedbackForm
from django.http import HttpResponseRedirect
from django.db import transaction
from django.urls import reverse_lazy
from django.contrib import messages


class FeedbackProfileView(ListView):
    model = Feedback
    template_name = 'profile_feedback.html'
    context_object_name = 'feedbacks'
    paginate_by = 2

    def get_queryset(self):
        return Feedback.objects.filter(user=self.request.user).order_by('-date_created')


class AddFeedbackView(LoginRequiredMixin, View):
    @transaction.atomic
    def post(self, request, product_id):
        form = AddFeedbackForm(request.POST, request.FILES)
        user = self.request.user
        product = Flowers.objects.get(id=product_id)
        cart = Cart.objects.get(user=user, flowers=product)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = user
            feedback.flowers = product
            feedback.rating = form.cleaned_data['rating']
            feedback.text = form.cleaned_data['text']
            feedback.image1 = form.cleaned_data['image1']
            feedback.image2 = form.cleaned_data['image2']
            feedback.image3 = form.cleaned_data['image3']
            feedback.save()
            cart.is_feedback = True
            cart.save()

            messages.add_message(request, messages.SUCCESS, 'Отзыв успешно отправлен.')
            return HttpResponseRedirect(reverse_lazy('feedback:feedback-profile'))

        messages.add_message(request, messages.SUCCESS, 'Отзыв не отправлен. Слишком длинный отзыв.')
        return HttpResponseRedirect(reverse_lazy('order:order-profile'))


class EditFeedbackView(LoginRequiredMixin, UpdateView):
    model = Feedback
    form_class = AddFeedbackForm
    template_name = 'edit_feedback.html'
    pk_url_kwarg = 'feedback_id'
    success_url = reverse_lazy('feedback:feedback-profile')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        feedback = Feedback.objects.get(id=self.kwargs['feedback_id'])
        context['feedback'] = feedback

        return context


class RemoveFeedbackView(LoginRequiredMixin, View):
    def get(self, request, feedback_id):
        user = self.request.user
        feedback = Feedback.objects.get(id=feedback_id)
        product = feedback.flowers
        cart = Cart.objects.get(user=user, flowers=product)
        try:
            feedback.delete()
            cart.is_feedback = False
            cart.save()
            messages.add_message(request, messages.SUCCESS, 'Отзыв успешно удален. Вы можете оставить новый отзыв.')

            return redirect(request.META['HTTP_REFERER'])
        except feedback.DoesNotExist:
            messages.add_message(request, messages.SUCCESS, 'Ошибка удаления отзыва. Попробуйте снова.')
