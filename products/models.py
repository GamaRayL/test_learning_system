from django.db import models

from config import settings
from constants import NULLABLE
from users.models import User


class Product(models.Model):
    """Модель продукта."""
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE, verbose_name='автор')
    students = models.ManyToManyField(User, related_name='products', verbose_name='студенты')
    name = models.CharField(max_length=255, verbose_name='название')
    start_datetime = models.DateTimeField(verbose_name='время начала')
    cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='стоимость')

    def __str__(self):
        return f'{self.name}. Автор: {self.author}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
