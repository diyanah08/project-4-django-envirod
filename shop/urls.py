from django.urls import path, include
from .views import catelog

urlpatterns = [
    path('catelog/', catelog, name ="catelog")
]