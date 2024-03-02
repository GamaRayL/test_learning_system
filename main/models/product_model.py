from config import settings
from django.db import models

from constants import NULLABLE


class Product(models.Model):
    """Модель продукта."""
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE, verbose_name='автор')
    name = models.CharField(max_length=255, verbose_name='название')
    start_datetime = models.DateTimeField(**NULLABLE, verbose_name='время начала')
    cost = models.DecimalField(max_digits=10, decimal_places=2, **NULLABLE, verbose_name='стоимость')
    min_users = models.PositiveIntegerField(default=1, verbose_name='минимальное количество пользователей')
    max_users = models.PositiveIntegerField(default=3, verbose_name='максимальное количество пользователей')

    def __str__(self):
        return f'{self.name}. Автор: {self.author}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
