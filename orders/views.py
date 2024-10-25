from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import OrderProductForm
from .models import Order

# Create your views here.
class MyOrdersView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = 'orders/myorder.html'
    context_object_name = 'order'
    
    def get_object(self, queryset = None):
        return Order.objects.filter(is_active=True, user=self.request.user).first()

class CreateOrderProdctView(LoginRequiredMixin, CreateView):

    template_name = 'orders/createorderproduct.html'
    form_class = OrderProductForm
    success_url = reverse_lazy('my_orders')
    
    def form_valid(self, form):
        order, _ = Order.objects.get_or_create(user=self.request.user, is_active=True)
        form.instance.order = order
        form.instance.quantity = 1
        form.save()
        return super().form_valid(form)
        

