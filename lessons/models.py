from django.db import models

from products.models import Product


class Lesson(models.Model):
    """Модель урока."""
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')
    name = models.CharField(max_length=255, verbose_name='название')
    video_link = models.URLField(verbose_name='ссылка на видео')

    def __str__(self):
        return f'{self.name} ({self.product.name})'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
