from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    slug = models.CharField(max_length=50, verbose_name='Слаг')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Discount(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название распродажи')
    percent = models.IntegerField(verbose_name='Размер скидки')

    class Meta:
        verbose_name = 'Распродажа'
        verbose_name_plural = 'Распродажи'

    def __str__(self):
        return self.title


class Flowers(models.Model):
    product = models.CharField(max_length=50, verbose_name='Продукт', blank=True, null=True)
    title = models.CharField(max_length=100, verbose_name='Название', blank=True, null=True,)
    text = models.CharField(max_length=1500, verbose_name='Описание', blank=True, null=True,)
    price = models.IntegerField(verbose_name='Цена')
    slug = models.CharField(max_length=50, verbose_name='Слаг', blank=True, null=True,)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    image = models.ImageField(upload_to="flowers_images", blank=True, null=True, verbose_name='Изображение')
    quantity = models.IntegerField(verbose_name='Количество', blank=True, null=True)
    is_discount = models.BooleanField(verbose_name='Скидка', default=False)
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE, verbose_name='Размер скидки', null=True)

    class Meta:
        verbose_name = 'Растение'
        verbose_name_plural = 'Растения'

    def __str__(self):
        return self.title

    def calculate_the_price(self):
        if self.is_discount:
            return int(self.price * ((100 - self.discount.percent) / 100))
        else:
            return int(self.price)








