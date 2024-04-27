from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import index_shop, contact_shop, product_info

app_name = CatalogConfig.name

urlpatterns = [
    path("", index_shop, name='products_list'),
    path("contacts/", contact_shop, name='contact_shop'),
    path("products/<int:pk>", product_info, name='product_info')
]
