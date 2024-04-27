import json

from django.core.management import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        with open('fixtures/category.json') as file:
            return json.load(file)

    @staticmethod
    def json_read_products():
        with open('fixtures/product.json') as f:
            return json.load(f)

    def handle(self, *args, **options):

        Product.objects.all().delete()
        Category.objects.all().delete()
        # for i in product_list:
        #     Product.objects.create(**i)

        product_for_create = []
        category_for_create = []
        # заполнение БД категорий продуктов
        for item in Command.json_read_categories():
            category_for_create.append(Category(**item))

        Category.objects.bulk_create(category_for_create)
        # заполнение БД продуктов
        for i in Command.json_read_products():
            product_for_create.append(Product(**i))

        Product.objects.bulk_create(product_for_create)
