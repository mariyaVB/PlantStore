# Generated by Django 4.2.1 on 2024-06-17 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_cartview'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CartView',
        ),
    ]