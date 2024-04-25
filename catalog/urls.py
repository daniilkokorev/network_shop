from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import index_shop, contact_shop, base_shop

app_name = CatalogConfig.name

urlpatterns = [
    path("", index_shop),
    path("contacts/", contact_shop),
    path("catalog/", base_shop)
]
