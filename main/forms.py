from django.forms import ModelForm
from django.utils.html import strip_tags
from .models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description']

    def clean_mood(self):
        mood = self.cleaned_data["mood"]
        return strip_tags(mood)

    def clean_feelings(self):
        feelings = self.cleaned_data["feelings"]
        return strip_tags(feelings)
