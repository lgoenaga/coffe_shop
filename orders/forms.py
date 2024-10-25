from django.forms import ModelForm

from .models import OrderProduct

class OrderProductForm(ModelForm):
    class Meta:
        model = OrderProduct
        fields = ["product"]
        
        

"""
    def save(self, order):
        data = self.cleaned_data
        order_product = OrderProduct.objects.create(
            product = data["product"],
            quantity = data["quantity"],
            order = order,
        )
        return order_product
"""      
