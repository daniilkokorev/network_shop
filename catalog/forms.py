from django.forms import ModelForm, ValidationError

from catalog.models import Product, Version
from common.views import StyleFormMixin


class ProductForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        exclude = ('author',)

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


class ProductModeratorForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        fields = ('is_published', 'category', 'description')


class VersionForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Version
        fields = ('number_version', 'name_version', 'indication_version')
