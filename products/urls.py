
from django.urls import path
from .views import ProductListAPI, productFormView, productListView, productsListView

urlpatterns = [
    path("agregar/", productFormView.as_view(), name="add_product"),
    path("listar/", productListView.as_view(), name="list_products"),
    path("", productsListView.as_view(), name="lists_products"),
    path("listar/<int:pk>/", productListView.as_view(), name="list_products"),
    path('api/', ProductListAPI.as_view(), name='api_products'),
]
