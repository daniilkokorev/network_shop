from django.urls import path

from stock.apps import StockConfig
from stock.views import StockCreateView, StockListView, StockDetailView, StockDeleteView, StockUpdateView

app_name = StockConfig.name

urlpatterns = [
    path("create/", StockCreateView.as_view(), name='create_stock'),
    path("", StockListView.as_view(), name='stock_list'),
    path("view/<int:pk>", StockDetailView.as_view(), name='stock_info'),
    path("edit/<int:pk>", StockUpdateView.as_view(), name='update_stock'),
    path("delete/<int:pk>", StockDeleteView.as_view(), name='delete_stock'),
]
