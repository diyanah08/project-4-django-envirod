from django.shortcuts import render,redirect,reverse
from .models import CartItem
from shop.models import Product

def view_cart(request):
    all_cart_items = CartItem.objects.filter(owner=request.user)
    return render(request, 'cart/cart.template.html',{
        'all_cart_items':all_cart_items
    })

def add_to_cart(request, product_id):
    
    product = Product.objects.get(pk=product_id)
    
    existing_cart_item = CartItem.objects.filter(owner=request.user, product=product).first()
    
    if existing_cart_item == None:
        new_cart_item = CartItem()
        new_cart_item.product = product
        new_cart_item.owner = request.user
        new_cart_item.quantity = 1
        new_cart_item.save()
    else:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    return redirect(reverse('catalog'))
    
def remove_from_cart(request, cart_item_id):

    existing_cart_item = CartItem.objects.get(pk=cart_item_id)
    existing_cart_item.quantity -= 1
    existing_cart_item.save()
    return redirect(reverse('view'))