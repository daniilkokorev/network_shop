from catalog.models import Category
from django.core.cache import cache
from config.settings import CACHE_ENABLED


def get_category_from_cache():
    """
    Функция для получения категорий из кэша
    """
    if not CACHE_ENABLED:
        category_list = cache.get("category_list")
        if not category_list:
            category_list = Category.objects.all()
            cache.set("category_list", category_list)
        return category_list
    else:
        return Category.objects.all()
