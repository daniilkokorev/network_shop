# Generated by Django 4.2.2 on 2024-05-29 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0014_rename_user_product_author"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={
                "ordering": ["name", "category"],
                "permissions": [
                    ("can_edit_publish", "Может изменять публикацию продукта"),
                    ("can_edit_description", "Может изменять описание продукта"),
                    ("can_edit_category", "Может изменять категорию продукта"),
                ],
                "verbose_name": "продукт",
                "verbose_name_plural": "продукты",
            },
        ),
        migrations.AddField(
            model_name="product",
            name="is_published",
            field=models.BooleanField(default=False, verbose_name="Опубликовано"),
        ),
    ]
