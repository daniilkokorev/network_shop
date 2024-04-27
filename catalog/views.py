from django.shortcuts import render, get_object_or_404

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
    product = get_object_or_404(Product, pk=pk)
    context = {"item": product}
    return render(request, "catalog/product_info.html", context)
