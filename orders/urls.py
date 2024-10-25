
from django.urls import path
from .views import CreateOrderProdctView, MyOrdersView


urlpatterns = [
    path('my-orden/', MyOrdersView.as_view(), name='my_orders'),
    path('agregar-producto/', CreateOrderProdctView.as_view(), name='create_order_product'),
]
