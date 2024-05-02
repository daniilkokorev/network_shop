from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from catalog.models import Product


# Create your views here.
# Создайте свои контроллеры здесь.


class ProductListView(ListView):
    """CBV класс-контроллер отображающий список продуктов"""
    model = Product

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)

        return queryset.filter(is_published=True)



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

    def get_object(self, queryset=None):
        """ Метод для счётчика просмотров продукта """
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()
        return self.object

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

    def form_valid(self, form):
        """ метод выводит slug продукта """
        if form.is_valid():
            new_prod = form.save()
            new_prod.slug = slugify(new_prod.name)
            new_prod.save()

        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    """контроллер редактирования продукта"""
    model = Product
    fields = ("name", "description", "picture", "category", "price_long", "updated_at")
    # success_url = reverse_lazy("catalog:products_list")

    def form_valid(self, form):
        """ метод выводит slug продукта """
        if form.is_valid():
            new_prod = form.save()
            new_prod.slug = slugify(new_prod.name)
            new_prod.save()

        return super().form_valid(form)

    def get_success_url(self):
        """ метод переопределяет запрос к url"""
        return reverse("catalog:product_info", kwargs={"pk": self.object.pk})


class ProductDeleteView(DeleteView):
    """контроллер удаления продукта"""
    model = Product
    success_url = reverse_lazy("catalog:products_list")


def toggle_activity(request, pk):
    """Функция для изменения статуса продукта"""
    product_item = get_object_or_404(Product, pk=pk)
    if product_item.is_available:
        product_item.is_available = False
    else:
        product_item.is_available = True

    product_item.save()

    return redirect(reverse("catalog:product_info", kwargs={"pk": pk}))
