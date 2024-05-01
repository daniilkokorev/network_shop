from django.db import models

# Create your models here.
# Создавайте свои модели здесь.

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
        auto_now_add=True,
        help_text="Введите дату последнего изменения"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ["name", "category"]
