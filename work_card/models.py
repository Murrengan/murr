from django.db import models


class WorkCard(models.Model):
    title = models.CharField(max_length=64, verbose_name='Заголовок')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    contact = models.CharField(max_length=64, null=True, blank=True, verbose_name='Контакты')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')
    city = models.CharField(max_length=64, null=True, blank=True, verbose_name='Город')
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Рубрика')

    class Meta:
        verbose_name_plural = 'Мурры'
        verbose_name = 'Мурр'
        ordering = ['-published']


class Rubric(models.Model):
    rubric = models.CharField(max_length=20, db_index=True, verbose_name='Рубрика')

    def __str__(self):
        return self.rubric

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['rubric']
