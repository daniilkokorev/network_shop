from django.forms import ModelForm, ValidationError
from django.forms.fields import BooleanField

from catalog.models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
