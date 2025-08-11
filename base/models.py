from django.contrib import admin
from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Название продукта'
        )
    description = models.TextField(
        verbose_name='Описание продукта'
    )

    info = models.URLField(
        verbose_name='информация',
        blank=True,     # чтобы поле было необязательным
        null=True
    )

    category = models.CharField(
        max_length=255,
        verbose_name='Категория продукта'
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Цена продукта'
    )
    delivery = models.BooleanField(
        default=False,
        verbose_name='Доставка'
    )
    image = models.ImageField(upload_to='products/', verbose_name='Изображение')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['title']