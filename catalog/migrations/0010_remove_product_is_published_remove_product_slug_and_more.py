# Generated by Django 5.0.4 on 2024-05-04 04:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_product_is_published_product_slug_product_view_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='is_published',
        ),
        migrations.RemoveField(
            model_name='product',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='product',
            name='view_count',
        ),
    ]
