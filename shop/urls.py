from django.urls import path, include
from .views import catalog

urlpatterns = [
    path('catalog/', catalog, name ="catalog")
]