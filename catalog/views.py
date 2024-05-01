from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView

from catalog.models import Product


# Create your views here.
# Создайте свои контроллеры здесь.


class ProductListView(ListView):
    """CBV класс-контроллер отображающий список продуктов"""
    model = Product


# def index_shop(request):
#     """ FBV функции-контроллер """
#     products = Product.objects.all()
#     context = {"products": products}
#     return render(request, "catalog/product_list.html", context)


class ContactView(TemplateView):
    """CBV класс-контроллер контактов"""
    template_name = "catalog/contact.html"

    def post_request(self, request, *args, **kwargs):
        if request.method == "POST":
            name = request.POST.get("name")
            phone = request.POST.get("phone")
            message = request.POST.get("message")
            print(f"{name}, {phone}, {message}")
        return render(request, self.template_name)


# def contact_shop(request):
#     if request.method == "POST":
#         name = request.POST.get("name")
#         phone = request.POST.get("phone")
#         message = request.POST.get("message")
#         print(f"{name}, {phone}, {message}")
#     return render(request, "catalog/contact.html")


class ProductDetailView(DetailView):
    """CBV класс-контроллер отображающий информацию о продукте"""
    model = Product

# def product_info(request, pk):
#     """ FBV функции-контроллер """
#     product = get_object_or_404(Product, pk=pk)
#     context = {"item": product}
#     return render(request, "catalog/product_detail.html", context)


class ProductCreateView(CreateView):
    """контроллер добавления продукта"""
    model = Product
    fields = ("name", "description", "picture", "category", "price_long")
    success_url = reverse_lazy("catalog:products_list")


class ProductUpdateView(UpdateView):
    """контроллер редактирования продукта"""
    model = Product
    fields = ("name", "description", "picture", "category", "price_long", "updated_at")
    success_url = reverse_lazy("catalog:products_list")

