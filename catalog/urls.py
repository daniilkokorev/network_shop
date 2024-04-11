from django.urls import path

from catalog.views import index_shop, contact_shop

urlpatterns = [
    path('', index_shop),
    path('contacts/', contact_shop)
]
