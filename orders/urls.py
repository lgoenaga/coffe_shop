
from django.urls import path

from products.views import productListView
from products.views import productFormView

urlpatterns = [
    path("agregar/", productFormView.as_view(), name="add_product"),
    path("listar/", productListView.as_view(), name="list_products"),
]
