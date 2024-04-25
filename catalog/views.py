from django.shortcuts import render

from catalog.models import Product


# Create your views here.
# Создайте свои контроллеры здесь.


def index_shop(request):
    return render(request, "catalog/index.html")


def contact_shop(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(f"{name}, {phone}, {message}")
    return render(request, "catalog/contact.html")


def base_shop(request):
    products = Product.objects.all()
    context = {"Products": products}
    return render(request, "catalog/base.html", context)
