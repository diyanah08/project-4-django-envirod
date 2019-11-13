from django.shortcuts import render
from .models import Product

# Create your views here.
def home(request):
    return render(request, 'shop/home.template.html')

def browse(request):
    all_products = Product.objects.all()
    return render(request, 'shop/browse.template.html', {
        'all_products': all_products
    })

def catalog(request):
    all_products = Product.objects.all()
    return render(request, 'shop/catelog.template.html', {
        'all_products': all_products
    })