from django.db import models


class Posts(models.Model):
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    text = models.TextField('Текст статьи')
    date = models.DateTimeField('Дата публикации', auto_now_add=True)

    def __str__(self):
        return f'новость: {self.title}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
