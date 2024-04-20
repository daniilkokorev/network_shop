from django.shortcuts import render

# Create your views here.


def index_shop(request):
    return render(request, "catalog/index.html")


def contact_shop(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(f"{name}, {phone}, {message}")
    return render(request, "catalog/contact.html")
