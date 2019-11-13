from django.urls import path, include
from .views import catalog, browse, home

urlpatterns = [
    path('', home, name ="home"),
    path('catalog/', catalog, name ="catalog"),
    path('browse/', browse, name="browse"),
]