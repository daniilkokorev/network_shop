from django.db import models

from catalog.models import NULLABLE


# Create your models here.
# Создавайте свои модели здесь.


class Stock(models.Model):
    """
    Класс для моделей новостных статей
    """
    name = models.CharField(
        max_length=150,
        verbose_name="Название статьи"
    )
    slug = models.CharField(
        max_length=150,
        verbose_name="slug",
        **NULLABLE
    )
    content = models.TextField(verbose_name="Содержание статьи")
    preview = models.ImageField(
        upload_to="stock/media",
        **NULLABLE,
        verbose_name="Изображение"
    )
    created_at = models.DateField(
        verbose_name="Дата создания",
        auto_now_add=True,
        **NULLABLE
    )
    is_published = models.BooleanField(
        default=True,
        verbose_name="Опубликовано"
    )
    view_count = models.IntegerField(
        default=0,
        verbose_name="Количество просмотров"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
