from django.contrib import admin

from catalog.models import Product, Category


# Register your models here.
# Регистрируйте своих моделей здесь.

# admin.site.register(Product)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name_product", "description_product", "picture_product", "category_product", "price_long", "created_at")
    list_filter = ("name_product",)
    search_fields = ("name_product",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
