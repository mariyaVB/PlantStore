# Generated by Django 4.2.1 on 2024-05-14 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flowers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flowers',
            name='text',
            field=models.CharField(max_length=1500, verbose_name='Описание'),
        ),
    ]
