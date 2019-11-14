from django.urls import path, include
from .views import login, logout, register, profile, editProfile

urlpatterns = [
    path('login/', login, name ="login"),
    path('logout/', logout, name ="logout"),
    path('register/', register, name ="register"),
    path('profile/', profile, name ="profile"),
    path('edit/', editProfile, name ="editProfile"),
    path('', include('django.contrib.auth.urls')),
]
