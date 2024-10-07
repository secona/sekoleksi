from django.forms import ModelForm, ValidationError
from django.utils.html import strip_tags
from .models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description']

    def clean_name(self):
        name = strip_tags(self.cleaned_data["name"])
        if not name:
            raise ValidationError("Name cannot be empty.")
        return name

    def clean_price(self):
        price = strip_tags(self.cleaned_data["price"])
        if not price:
            raise ValidationError("Price cannot be empty.")
        return price

    def clean_description(self):
        description = strip_tags(self.cleaned_data["description"])
        if not description:
            raise ValidationError("Description cannot be empty.")
        return description
