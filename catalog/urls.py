from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import ContactView, ProductListView, ProductDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path("", ProductListView.as_view(), name='products_list'),
    path("contacts/", ContactView.as_view(), name='contact_shop'),
    path("products/<int:pk>", ProductDetailView.as_view(), name='product_info')
]
