# Generated by Django 5.0.4 on 2024-04-23 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0002_category_alter_product_options_product_created_at_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={
                "ordering": ["name", "category"],
                "verbose_name": "продукт",
                "verbose_name_plural": "продукты",
            },
        ),
        migrations.RenameField(
            model_name="category",
            old_name="description_category",
            new_name="description",
        ),
        migrations.RenameField(
            model_name="category",
            old_name="name_category",
            new_name="name",
        ),
        migrations.RenameField(
            model_name="product",
            old_name="category_product",
            new_name="category",
        ),
        migrations.RenameField(
            model_name="product",
            old_name="description_product",
            new_name="description",
        ),
        migrations.RenameField(
            model_name="product",
            old_name="name_product",
            new_name="name",
        ),
        migrations.RenameField(
            model_name="product",
            old_name="picture_product",
            new_name="picture",
        ),
    ]
