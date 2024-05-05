from django.contrib import admin

from stock.models import Stock


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ("id", "name", 'content', "is_published")
    list_filter = ("name", "is_published")
    search_fields = ("name", 'content')
