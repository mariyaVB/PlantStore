# Generated by Django 4.2.1 on 2024-07-16 18:47

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('flowers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='Оценка')),
                ('text', models.CharField(max_length=300, verbose_name='Отзыв')),
                ('image1', models.ImageField(blank=True, null=True, upload_to='feedback_images/')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='feedback_images/')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='feedback_images/')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания отзыва')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Дата редактирования отзыва')),
                ('flowers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flowers.flowers', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
    ]
