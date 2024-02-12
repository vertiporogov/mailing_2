from django.db import models

from users.models import User

NULLABLE = {'null': True, 'blank': True}


class Client(models.Model):
    email = models.EmailField(verbose_name='Почта клиента', unique=True)
    name = models.CharField(max_length=150, verbose_name='Имя клиента')
    comment = models.TextField(**NULLABLE, verbose_name='Комментарий')

    owner = models.ForeignKey(User, **NULLABLE, on_delete=models.SET_NULL, verbose_name='пользователь')

    def __str__(self):
        return f'{self.name} ({self.email})'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class MailingMassage(models.Model):
    name_massage = models.CharField(max_length=50, verbose_name='название письма')
    topic_massage = models.CharField(max_length=200, **NULLABLE, verbose_name='тема письма')
    body_massage = models.TextField(verbose_name='тело письма')

    owner = models.ForeignKey(User, **NULLABLE, on_delete=models.SET_NULL, verbose_name='пользователь')

    def __str__(self):
        return f'{self.name_massage}'

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'


class MailingModel(models.Model):
    email = models.ManyToManyField(Client, verbose_name='клиент рассылки')
    name_mailing = models.CharField(max_length=100, verbose_name='название рассылки')
    start_time = models.DateTimeField(auto_now=False, auto_now_add=False, verbose_name='начало рассылки')
    end_time = models.DateTimeField(auto_now=False, auto_now_add=False, verbose_name='окончание рассылки')
    send = models.BooleanField(default=False, verbose_name='рассылка запущена')
    is_activ = models.BooleanField(default=False, verbose_name='рассылка активна')
    send_end = models.BooleanField(default=False, verbose_name='рассылка завершена')
    body_massage = models.ForeignKey(MailingMassage, on_delete=models.SET_NULL, **NULLABLE,
                                     verbose_name='текст рассылки')

    owner = models.ForeignKey(User, **NULLABLE, on_delete=models.SET_NULL, verbose_name='пользователь')

    def __str__(self):
        return f'{self.name_mailing} ({self.start_time} - {self.end_time})'

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'


class MailingList(models.Model):
    name_mailing = models.ForeignKey(MailingModel, on_delete=models.CASCADE, verbose_name='рассылка')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='клтиент')

    owner = models.ForeignKey(User, **NULLABLE, on_delete=models.SET_NULL, verbose_name='пользователь')

    def __str__(self):
        return f'{self.name_mailing} - {self.client}'

    class Meta:
        verbose_name = 'письмо'
        verbose_name_plural = 'письма'


class MailingLogs(models.Model):
    mailing = models.ForeignKey(MailingModel, on_delete=models.CASCADE, **NULLABLE, verbose_name='рассылка')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='клиент рассылки', **NULLABLE)

    last_mailing_time = models.DateTimeField(auto_now=True, verbose_name='время последней рассылки')
    status = models.CharField(max_length=50, verbose_name='статус попытки', null=True)
    response = models.CharField(max_length=200, verbose_name="ответ почтового сервера", **NULLABLE)

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.last_mail_time = None

    def __str__(self):
        return f'Отправлено: {self.last_mailing_time}, ' \
               f'Статус: {self.status}'

    class Meta:
        verbose_name = 'log'
        verbose_name_plural = 'logs'
