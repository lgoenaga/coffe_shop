from django.urls import reverse_lazy
from django.views import generic

from products.forms import ProductForm
from products.models import Product

class productFormView(generic.FormView):
    template_name = 'products/add_product.html'
    form_class = ProductForm
    success_url = reverse_lazy('add_product')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
      
class productListView(generic.ListView):
    template_name = 'products/list_products.html'
    model = Product
    context_object_name = 'products'
    #paginate_by = 10
    #ordering = ['name']
    
    def get_queryset(self):
        return Product.objects.filter(available=True)

class productsListView(generic.ListView):
    template_name = 'products/lists_products.html'
    model = Product
    context_object_name = 'products'
    # paginate_by = 10
    # ordering = ['name']
    
    def get_queryset(self):
        return Product.objects.filter(available=True)