from django.db import models

from users.models import User

NULLABLE = {"blank": True, "null": True}


class Category(models.Model):
    """
    Класс для моделей категории продуктов
    """
    name = models.CharField(
        max_length=150, verbose_name="Наименование категории"
    )
    description = models.TextField(verbose_name="Описание категории")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"


class Product(models.Model):
    """
    Класс для моделей продуктов
    """
    name = models.CharField(
        max_length=150,
        verbose_name="Наименование продукта",
        help_text="Введите название продукта",
    )
    description = models.TextField(
        verbose_name="Описание продукта", help_text="Введите описание продукта"
    )
    picture = models.ImageField(
        upload_to="catalog/media",
        verbose_name="Изображение продукта",
        **NULLABLE,
        help_text="Загрузите изображение продукта"
    )
    category = models.ForeignKey(
        "Category",
        on_delete=models.SET_NULL,
        verbose_name="Категория продукта",
        help_text="Введите категорию продукта",
        **NULLABLE,
        related_name="products"
    )
    price_long = models.IntegerField(
        verbose_name="Цена продукта", help_text="Введите цену за продукт", **NULLABLE
    )
    created_at = models.DateField(
        verbose_name="Дата создания",
        help_text="Введите дату загрузки продукта",
        auto_now_add=True,
        **NULLABLE
    )
    updated_at = models.DateField(
        verbose_name="Дата последнего изменения",
        **NULLABLE,
        help_text="Введите дату последнего изменения"
    )
    is_available = models.BooleanField(
        default=True,
        verbose_name="Доступен",
        help_text="Укажите, доступен ли продукт",
    )
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, verbose_name="Создан пользователем", **NULLABLE
    )
    is_published = models.BooleanField(
        default=False,
        verbose_name="Опубликовано"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ["name", "category"]
        permissions = [
            ("can_edit_publish", "Может изменять публикацию продукта"),
            ("can_edit_description", "Может изменять описание продукта"),
            ("can_edit_category", "Может изменять категорию продукта"),
        ]


class Version(models.Model):
    """
    Класс для моделей версий продуктов
    """
    product = models.ForeignKey(
        to=Product,
        on_delete=models.CASCADE,
        verbose_name="Продукт",
        related_name="version"
    )
    number_version = models.IntegerField(default=1, verbose_name="Номер версии")
    name_version = models.CharField(max_length=150, verbose_name="Название версии")
    indication_version = models.BooleanField(default=False, verbose_name="Признак версии")

    class Meta:
        verbose_name = "Версия"
        verbose_name_plural = "Версии"

    def __str__(self):
        return f'{self.name_version}'
