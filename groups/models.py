from django.core.exceptions import ValidationError
from django.db import models

from products.models import Product
from users.models import User


class Group(models.Model):
    """Модель группы."""
    students = models.ManyToManyField(User, verbose_name='ученики')
    name = models.CharField(max_length=255, verbose_name='название')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')
    min_users = models.PositiveIntegerField(verbose_name='минимальное количество пользователей')
    max_users = models.PositiveIntegerField(verbose_name='максимальное количество пользователей')

    def __str__(self):
        return f'{self.name}. ({self.min_users} - {self.max_users})'

    class Meta:
        verbose_name = 'группа'
        verbose_name_plural = 'группы'
