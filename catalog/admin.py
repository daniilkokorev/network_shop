from django.contrib import admin

from catalog.models import Product, Category, Version


# Register your models here.
# Регистрируйте своих моделей здесь.

# admin.site.register(Product)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', "name", 'description', "price_long", "category")
    list_filter = ("category",)
    search_fields = ("name", 'description')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'number_version', 'name_version', 'indication_version')
