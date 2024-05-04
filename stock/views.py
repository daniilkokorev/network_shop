from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from pytils.translit import slugify

from stock.models import Stock


# Create your views here.
# Создайте свои контроллеры здесь.

class StockCreateView(CreateView):
    """контроллер создания статьи"""
    model = Stock
    fields = ("name", "content", "preview", "is_published")
    success_url = reverse_lazy("stock:stock_list")

    def form_valid(self, form):
        """ метод выводит slug статьи """
        if form.is_valid():
            new_stock = form.save()
            new_stock.slug = slugify(new_stock.name)
            new_stock.save()

        return super().form_valid(form)


class StockListView(ListView):
    """CBV класс-контроллер отображающий список статей"""
    model = Stock

    def get_queryset(self, *args, **kwargs):
        """ Метод выводит только опубликованные статьи """
        queryset = super().get_queryset(*args, **kwargs)

        return queryset.filter(is_published=True)


class StockDetailView(DetailView):
    """CBV класс-контроллер отображающий информацию о статье"""
    model = Stock

    def get_object(self, queryset=None):
        """ Метод для счётчика просмотров продукта """
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()
        return self.object


class StockDeleteView(DeleteView):
    """контроллер удаления статьи"""
    model = Stock
    success_url = reverse_lazy("stock:stock_list")


class StockUpdateView(UpdateView):
    """контроллер редактирования статьи"""
    model = Stock
    fields = ("name", "content", "preview", "is_published")
    # success_url = reverse_lazy("stock:stock_list")

    def get_success_url(self):
        """ метод переопределяет запрос к url"""
        return reverse("stock:stock_info", kwargs={"pk": self.object.pk})
