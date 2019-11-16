from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from .forms import ItemForm
from personalise.models import Item, Category
from cart.models import CartItem

# Create your views here.
def show_products(request):
    items = Item.objects.all()
    return render(request, "personalise/show_products.template.html", {
        "items":items
    })


# def personalise_product(request):
#     if request.method == "POST":
#         form = ItemForm(request.POST)
#         if form.is_valid():
#             form.save()
#             items = Item.objects.all()
#             return redirect(reverse('show_products'), {
#                 "items":items
#             })  
#         else:
#             return render(request, "personalise/personalise_form.template.html", {
#                 "form":form
#             })
#     else:
#         form = ItemForm()
#         return render(request, "personalise/personalise_form.template.html", {
#                 "form":form
#         })
        
def personalise_product(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            items = Item.objects.all()
            return redirect(reverse('show_products'), {
                "items":items
            })  
        else:
            return render(request, "personalise/personalise_form.template.html", {
                "form":form
            })
    else:
        form = ItemForm()
        return render(request, "personalise/personalise_form.template.html", {
                "form":form
        })