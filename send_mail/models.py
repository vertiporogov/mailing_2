from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Client(models.Model):
    email = models.EmailField(verbose_name='Почта клиента', unique=True)
    name = models.CharField(max_length=150, verbose_name='Имя клиента')
    comment = models.TextField(**NULLABLE, verbose_name='Комментарий')

    def __str__(self):
        return f'{self.full_name} ({self.email})'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class MailingMassage(models.Model):
    name_massage = models.CharField(max_length=50, verbose_name='название письма')
    topic_massage = models.CharField(max_length=200, **NULLABLE, verbose_name='тема письма')
    body_massage = models.TextField(verbose_name='тело письма')

    def __str__(self):
        return f'{self.name_massage}'

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'


class MailingModel(models.Model):
    name_mailing = models.CharField(max_length=100, verbose_name='название рассылки')
    start_time = models.DateTimeField(auto_now=False, auto_now_add=False, verbose_name='начало рассылки')
    end_time = models.DateTimeField(auto_now=False, auto_now_add=False, verbose_name='окончание рассылки')
    send = models.BooleanField(default=False, verbose_name='рассылка запущена')
    is_activ = models.BooleanField(default=False, verbose_name='рассылка активна')
    send_end = models.BooleanField(default=False, verbose_name='рассылка завершена')
    body_massage = models.ForeignKey(MailingMassage, on_delete=models.SET_NULL, **NULLABLE,
                                     verbose_name='текст рассылки')

    def __str__(self):
        return f'{self.name_mailing} ({self.start_time} - {self.end_time})'

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'


class MailingList(models.Model):
    mailing_model = models.ForeignKey(MailingModel, on_delete=models.CASCADE, verbose_name='рассылка')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='клтиент')

    def __str__(self):
        return f'{self.mailing_model} - {self.client}'

    class Meta:
        verbose_name = 'письмо'
        verbose_name_plural = 'письма'
