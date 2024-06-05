from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import ContactView, ProductListView, ProductDetailView, toggle_activity, ProductCreateView, \
    ProductUpdateView, ProductDeleteView, CategoryListView, CategoryDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path("", ProductListView.as_view(), name='products_list'),
    path("contacts/", ContactView.as_view(), name='contact_shop'),
    path("products/<int:pk>", cache_page(60)(ProductDetailView.as_view()), name='product_info'),
    path("activity/<int:pk>", toggle_activity, name='activity_product'),
    path("create/", ProductCreateView.as_view(), name='create_product'),
    path("edit/<int:pk>", ProductUpdateView.as_view(), name='update_product'),
    path("delete/<int:pk>", ProductDeleteView.as_view(), name='delete_product'),
    path('catalog/', CategoryListView.as_view(), name='category_list'),
    path('category/<int:pk>', CategoryDetailView.as_view(), name='category_detail'),
]
