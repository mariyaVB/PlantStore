# Generated by Django 4.2.1 on 2024-06-12 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flowers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flowers',
            name='product',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Продукт'),
        ),
    ]