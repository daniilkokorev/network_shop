from django.forms import ModelForm, ValidationError
from django.forms.fields import BooleanField

from catalog.models import Product
from common.views import StyleFormMixin


class ProductForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def clean_name(self):
        """
        Метод исключает попадание запрещённых слов в название продукта
        """
        name = self.cleaned_data.get("name")
        forbidden_words = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно",
                           "обман", "полиция", "радар"]
        for word in forbidden_words:
            if word in name.lower():
                raise ValidationError(
                    "Нельзя использовать запрещённые слова"
                )
        return name

    def clean_description(self):
        """
        Метод исключает попадание запрещённых слов в описание продукта
        """
        description = self.cleaned_data.get("description")
        forbidden_words = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно",
                           "обман", "полиция", "радар"]
        for word in forbidden_words:
            if word in description.lower():
                raise ValidationError(
                    "Нельзя использовать запрещённые слова"
                )
        return description
