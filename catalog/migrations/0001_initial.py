# Generated by Django 5.0.4 on 2024-04-16 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name_product",
                    models.CharField(max_length=150, verbose_name="Наименование"),
                ),
                ("description_product", models.TextField()),
                (
                    "picture_product",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="products/",
                        verbose_name="Изображение",
                    ),
                ),
            ],
            options={
                "verbose_name": "продукт",
                "verbose_name_plural": "продукты",
            },
        ),
    ]
