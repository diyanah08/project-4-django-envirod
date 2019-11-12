from django.urls import path
from .views import payment_form, pay

urlpatterns = [
    path('payment_form', payment_form, name="payment_form"),
    path('pay', pay, name="pay")
]