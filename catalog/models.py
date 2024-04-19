from django.db import models

# Create your models here.
# Создавайте свои модели здесь.

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    name_product = models.CharField(max_length=150, verbose_name='Наименование')
    description_product = models.TextField(verbose_name='Описание')
    picture_product = models.ImageField(upload_to='products/', verbose_name='Изображение', **NULLABLE)
    category_product = models.ForeignKey()
    price_long = models.IntegerField()
    created_at = models.DateField()
    updated_at = models.DateField()

    def __str__(self):
        return f'{self.name_product}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
