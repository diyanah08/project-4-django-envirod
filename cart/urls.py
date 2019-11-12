from django.urls import path, include
from .views import view_cart, add_to_cart, remove_from_cart

urlpatterns = [
    path('view', view_cart, name='view'),
    path('add_to_cart/<product_id>', add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<cart_item_id>', remove_from_cart, name='remove_from_cart')
]