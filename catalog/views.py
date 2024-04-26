from django.shortcuts import render

from catalog.models import Product


# Create your views here.
# Создайте свои контроллеры здесь.


def index_shop(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "catalog/products_list.html", context)


def contact_shop(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(f"{name}, {phone}, {message}")
    return render(request, "catalog/contact.html")


def product_info(request, pk):
    product = Product.objects.get(pk=pk)
    context = {"product": product}
    return render(request, "catalog/product_info.html", context)
