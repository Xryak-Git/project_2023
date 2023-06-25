from .models import Product
from django.forms import ModelForm, TextInput, NumberInput, DateTimeInput


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'price', 'date', 'image']

        widgets = {
            'title': TextInput(attrs={
                'placeholder': 'Title'
            }),
            'price': NumberInput(attrs={
                'placeholder': 'Price'
            }),
            'date': DateTimeInput(attrs={
                'placeholder': 'Date'
            }),
        }

