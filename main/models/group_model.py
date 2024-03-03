from django.db import models


class Group(models.Model):
    """Модель группы."""
    students = models.ManyToManyField('users.User', verbose_name='ученики')
    name = models.CharField(max_length=255, verbose_name='название')
    product = models.ForeignKey('main.Product', on_delete=models.CASCADE, related_name='groups', verbose_name='продукт')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'группа'
        verbose_name_plural = 'группы'
