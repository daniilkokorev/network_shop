from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm, VersionForm, ProductModeratorForm
from catalog.models import Product, Version, Category
from catalog.services import get_category_from_cache


class ProductListView(ListView):
    """CBV класс-контроллер отображающий список продуктов"""
    model = Product


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


class ProductDetailView(DetailView, LoginRequiredMixin):
    """CBV класс-контроллер отображающий информацию о продукте"""
    model = Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    """контроллер добавления продукта"""
    form_class = ProductForm
    model = Product
    success_url = reverse_lazy("catalog:products_list")

    def get_context_data(self, **kwargs):
        """
        Метод добавляет в контекст форму для добавления версий продукта
        """
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, VersionForm, extra=1)
        if self.request.method == "POST":
            context_data["formset"] = VersionFormset(self.request.POST)
        else:
            context_data["formset"] = VersionFormset()
        return context_data

    def form_valid(self, form):
        if form.is_valid:
            new_object = form.save(commit=False)
            new_object.author = self.request.user
            new_object.save()
            return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    """контроллер редактирования продукта"""
    form_class = ProductForm
    model = Product

    def get_success_url(self):
        """ метод переопределяет запрос к url"""
        return reverse("catalog:product_info", kwargs={"pk": self.object.pk})

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, VersionForm, extra=1)
        if self.request.method == "POST":
            context_data["formset"] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data["formset"] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))

    def get_form_class(self):
        """
        Метод определяет права доступа пользователя
        """
        user = self.request.user
        if user == self.object.author:
            return ProductForm
        if (user.has_perm("catalog.can_edit_publish") and user.has_perm("catalog.can_edit_description")
                and user.has_perm("catalog.can_edit_category")):
            return ProductModeratorForm
        raise PermissionDenied


class ProductDeleteView(LoginRequiredMixin, DeleteView):
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


class CategoryListView(ListView):
    """CBV класс-контроллер отображающий список категорий"""
    model = Category
    success_url = reverse_lazy("catalog:category_list")

    def get_queryset(self):
        """
        Метод получает категории из кэша
        """
        return get_category_from_cache()


class CategoryDetailView(DetailView, LoginRequiredMixin):
    """CBV класс-контроллер отображающий информацию о категории"""
    model = Category
    success_url = reverse_lazy("catalog:category_detail")
