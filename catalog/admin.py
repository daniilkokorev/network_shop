from django.contrib import admin

from catalog.models import Product, Category


# Register your models here.
# Регистрируйте своих моделей здесь.

# admin.site.register(Product)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', "name_product", 'description_product', "price_long", "category_product",)
    list_filter = ("category_product",)
    search_fields = ("name_product", 'description_product')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_category', 'description_category')
