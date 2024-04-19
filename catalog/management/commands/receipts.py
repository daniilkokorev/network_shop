from django.core.management import BaseCommand

from catalog.models import Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        product_list = [
            {'name_product': 'Насос', 'description_product': 'УНБ-600'},
            {'name_product': 'ФЗ', 'description_product': 'Фрез торцевой'}
        ]

        # for i in product_list:
        #     Product.objects.create(**i)

        product_for_create = []
        for i in product_list:
            product_for_create.append(Product(**i))

        Product.objects.bulk_create(product_for_create)
