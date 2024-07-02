from django import forms
from feedback.models import Feedback
from django.core.exceptions import ValidationError


class AddFeedbackForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={'cols': 80, 'rows': 5,
                                                        'class': 'form-feedback-text',
                                                        'placeholder': 'Ваш отзыв'})
                           )
    image1 = forms.ImageField(required=False)
    image2 = forms.ImageField(required=False)
    image3 = forms.ImageField(required=False)

    class Meta:
        model = Feedback
        fields = ['rating', 'text', 'image1', 'image2', 'image3']
        widgets = {
            'rating': forms.HiddenInput(attrs={'id': 'hiddenRating', 'value': 0, 'name': 'rating'})
        }

    def clean_text(self):
        text = self.cleaned_data['text']
        if len(text) == 0:
            self.add_error('text', 'Короткий отзыв.')
            raise ValidationError('Короткий отзыв.')
        if len(text) > 300:
            self.add_error('text', 'Отзыв превышает 300 символов.')
            raise ValidationError('Отзыв превышает 300 символов.')
        return text

    def clean_rating(self):
        rating = self.cleaned_data['rating']
        if not rating:
            self.add_error('rating', 'Оценка не указана.')
            raise ValidationError('Оценка не указана.')
        try:
            rating = int(rating)
        except ValueError:
            raise ValidationError('Неверный формат оценки.')
        if not 1 <= rating <= 5:
            raise ValidationError('Оценка должна быть от 1 до 5.')
        return rating
