from django.contrib import admin

from catalog.models import Product

# Register your models here.
# Регистрируйте своих моделей здесь.

# admin.site.register(Product)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name_product', 'description_product')
    list_filter = ('name_product',)
    search_fields = ('name_product',)
