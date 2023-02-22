from django.contrib.auth.models import AbstractUser
from django.db import models


NULLABLE = {'blank': True, 'null': True}

class User(AbstractUser):
#    username = models.CharField(max_length=150, null=True, unique=True, verbose_name='Имя пользоателя')
    username = None
    email = models.EmailField(
        max_length=150,
        verbose_name='Почта',
        unique=True
    )
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    town = models.CharField(max_length=100, verbose_name='Город')
    avatar = models.ImageField(upload_to='image/', verbose_name='Аватарка', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.email} {self.phone} {self.town}'

