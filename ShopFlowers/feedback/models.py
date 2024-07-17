from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from flowers.models import Flowers
from users.models import User


class FeedbackQuerySet(models.QuerySet):
    def rating_mean(self):
        if self:
            return f'⭐ {sum(feedback.rating for feedback in self) / self.count()}'
        else:
            return f'⭐ 0'

    def feedback_count(self):
        feedback_count = int(self.count())
        if feedback_count == 0:
            return f'Нет отзывов'
        elif feedback_count % 10 == 1 and feedback_count % 100 != 11:
            return f'{feedback_count} отзыв'
        elif 2 <= feedback_count % 10 <= 4 and (feedback_count % 100 < 10 or feedback_count % 100 >= 20):
            return f'{feedback_count} отзыва'
        else:
            return f'{feedback_count} отзывов'


class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    flowers = models.ForeignKey(Flowers, on_delete=models.CASCADE, verbose_name='Товар')
    rating = models.IntegerField(default=0, verbose_name='Оценка',
                                 validators=[
                                     MinValueValidator(0),
                                     MaxValueValidator(5)
                                 ])
    text = models.CharField(max_length=300, verbose_name='Отзыв')
    image1 = models.ImageField(upload_to='feedback_images/', blank=True, null=True)
    image2 = models.ImageField(upload_to='feedback_images/', blank=True, null=True)
    image3 = models.ImageField(upload_to='feedback_images/', blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания отзыва')
    date_updated = models.DateTimeField(auto_now=True, verbose_name='Дата редактирования отзыва')

    objects = FeedbackQuerySet.as_manager()

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def rating_stars(self):
        return self.rating * '⭐'


