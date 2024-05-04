from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, TemplateView


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


def toggle_activity(request, pk):
    """Функция для изменения статуса продукта"""
    product_item = get_object_or_404(Product, pk=pk)
    if product_item.is_available:
        product_item.is_available = False
    else:
        product_item.is_available = True

    product_item.save()

    return redirect(reverse("catalog:product_info", kwargs={"pk": pk}))
