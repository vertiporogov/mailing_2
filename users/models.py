from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'null': True, 'blank': True}

class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='email')
    token = models.CharField(max_length=50, **NULLABLE, unique=True, verbose_name='токен')

    phone = models.CharField(max_length=35, **NULLABLE, verbose_name='номер телефона')
    avatar = models.ImageField(upload_to='users/', **NULLABLE, verbose_name='аватар')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
