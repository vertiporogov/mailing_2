from django.contrib.auth.models import AbstractUser
from django.db import models

from send_mail.models import NULLABLE


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='email')
    token = models.CharField(max_length=50, **NULLABLE, unique=True, verbose_name='токен')

    phone = models.CharField(max_length=35, **NULLABLE, verbose_name='номер телефона')
    avatar = models.ImageField(upload_to='users/', **NULLABLE, verbose_name='аватар')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
