from django.db import models


class Subscribe(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='пользователь')
    product = models.ForeignKey('main.Product', on_delete=models.CASCADE, verbose_name='продукт')
    is_active = models.BooleanField(default=True, verbose_name='статус')

    class Meta:
        unique_together = ('user', 'product')

        verbose_name = 'подписка'
        verbose_name_plural = 'подписки'
