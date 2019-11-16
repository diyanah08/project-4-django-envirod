from django.urls import path, include
from .views import personalise_product, show_products

urlpatterns = [
    path('personalise', personalise_product, name="personalise_product"),
    path('show_products', show_products, name="show_products")
]