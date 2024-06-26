# Generated by Django 5.0.4 on 2024-05-02 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0008_product_is_available"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="is_published",
            field=models.BooleanField(default=True, verbose_name="Опубликован"),
        ),
        migrations.AddField(
            model_name="product",
            name="slug",
            field=models.CharField(
                blank=True, max_length=150, null=True, verbose_name="slug"
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="view_count",
            field=models.IntegerField(default=0, verbose_name="Количество просмотров"),
        ),
    ]
