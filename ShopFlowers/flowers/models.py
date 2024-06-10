from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    slug = models.CharField(max_length=50, verbose_name='Слаг')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Flowers(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    text = models.CharField(max_length=1500, verbose_name='Описание')
    price = models.IntegerField(verbose_name='Цена')
    slug = models.CharField(max_length=50, verbose_name='Слаг')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    image = models.ImageField(upload_to="flowers_images", blank=True, null=True, verbose_name='Изображение')
    quantity = models.IntegerField(verbose_name='Количество', blank=True, null=True)

    class Meta:
        verbose_name = 'Растение'
        verbose_name_plural = 'Растения'

    def __str__(self):
        return self.title


# class CategoryPots(models.Model):
#     title = models.CharField(max_length=50, verbose_name='Название')
#     slug = models.CharField(max_length=50, verbose_name='Слаг')
#
#     class Meta:
#         verbose_name = 'Категория'
#         verbose_name_plural = 'Категории'
#
#     def __str__(self):
#         return self.title


class FlowerPots(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    text = models.CharField(max_length=1500, verbose_name='Описание')
    image = models.ImageField(upload_to="flowerpots_images", blank=True, null=True, verbose_name='Изображение')
    price = models.IntegerField(verbose_name='Цена')
    quantity = models.IntegerField(verbose_name='Количество', blank=True, null=True)
    slug = models.CharField(max_length=50, verbose_name='Слаг')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')

    class Meta:
        verbose_name = 'Горшок, кашпо'
        verbose_name_plural = 'Горшки, кашпо'

    def __str__(self):
        return self.title


# class CategoryCare(models.Model):
#     title = models.CharField(max_length=50, verbose_name='Название')
#     slug = models.CharField(max_length=50, verbose_name='Слаг')
#
#     class Meta:
#         verbose_name = 'Категория'
#         verbose_name_plural = 'Категории'
#
#     def __str__(self):
#         return self.title


class FlowersCare(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    text = models.CharField(max_length=1500, verbose_name='Описание')
    image = models.ImageField(upload_to="flowers_care_images", blank=True, null=True, verbose_name='Изображение')
    price = models.IntegerField(verbose_name='Цена')
    quantity = models.IntegerField(verbose_name='Количество', blank=True, null=True)
    slug = models.CharField(max_length=50, verbose_name='Слаг')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')

    class Meta:
        verbose_name = 'Удобрение'
        verbose_name_plural = 'Удобрения'

    def __str__(self):
        return self.title


