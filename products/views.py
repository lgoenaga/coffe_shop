from django.urls import reverse_lazy
from django.views import generic

from products.forms import ProductForm
from products.models import Product

from rest_framework.views import APIView
from rest_framework.response import Response

from products.serializers import ProductSerializer

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
    
    
class ProductListAPI(APIView):
    authentication_classes = []
    permission_classes = []
    
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)