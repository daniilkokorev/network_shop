from django.contrib import admin

from catalog.models import Product, Category


# Register your models here.
# Регистрируйте своих моделей здесь.

# admin.site.register(Product)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', "name", 'description', "price_long", "category",)
    list_filter = ("category",)
    search_fields = ("name", 'description')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
