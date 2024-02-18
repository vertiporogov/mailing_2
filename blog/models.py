from django.db import models

NULLABLE = {'blank': True, 'null': True}


class MailingBlog(models.Model):
    """Модель блога"""
    title = models.CharField(max_length=100, verbose_name='заголовок')
    body = models.TextField(verbose_name='содержимое блога')
    image = models.ImageField(upload_to='blog/', **NULLABLE, verbose_name='изображение')
    views_count = models.PositiveIntegerField(default=0, verbose_name='количество просмотров')
    creation_date = models.DateTimeField(auto_now_add=True, **NULLABLE, verbose_name='дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'
