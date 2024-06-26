# Generated by Django 4.2.1 on 2024-06-25 13:50

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('flowers', '0002_flowers_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagesFeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', models.ImageField(blank=True, null=True, upload_to='feedback_images/')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='feedback_images/')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='feedback_images/')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('text', models.CharField(max_length=30)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('flowers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flowers.flowers')),
                ('images_feedback', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedback.imagesfeedback')),
            ],
        ),
    ]
