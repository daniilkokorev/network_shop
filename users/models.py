from django.contrib.auth.models import AbstractUser
from django.db import models

from catalog.models import NULLABLE


class User(AbstractUser):
    """
    Класс для моделей пользователей
    """
    username = None
    email = models.EmailField(unique=True, verbose_name='Почта')

    avatar = models.ImageField(upload_to="user/media", **NULLABLE, verbose_name="Аватар")
    phone = models.CharField(max_length=35, verbose_name='Телефон')
    country = models.CharField(max_length=50, verbose_name='Страна')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
