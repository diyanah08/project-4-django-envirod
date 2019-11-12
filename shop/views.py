from django.shortcuts import render
from .models import Product

# Create your views here.
def catelog(request):
    all_products = Product.objects.all()
    return render(request, 'shop/catelog.template.html', {
        'all_products': all_products
    })