from django.db import models

NULLABLE = {'null': True, 'blank': True}

class Client(models.Model):
    email = models.EmailField(verbose_name='Почта клиента', unique=True)
    name = models.CharField(max_length=150, verbose_name='Имя клиента')
    comment = models.TextField(**NULLABLE)
