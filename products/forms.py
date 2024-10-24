from django import forms
from .models import Product

class ProductForm(forms.Form):
    name = forms.CharField(label="Nombre", max_length=200, label_suffix=":", required=True)
    description = forms.CharField(label="Descripción", max_length=500, label_suffix=":", required=True)
    price = forms.DecimalField(label="Precio", max_digits=10, decimal_places=2, label_suffix=":", required=True)
    available = forms.BooleanField(label="Disponible", initial=True, required=False, label_suffix=":")
    photo = forms.ImageField(label="Foto", required=False, label_suffix=":")
    
    def save(self):
        data = self.cleaned_data
        product = Product.objects.create(
            name = data["name"],
            description = data["description"],
            price = data["price"],
            available = data["available"],
            photo = data["photo"],
        )
        return product
