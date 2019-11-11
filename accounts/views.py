from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import auth, messages
from .forms import UserLoginForm

# Create your views here.
def home(request):
    return render(request, 'base.template.html')
    
def logout(request):
    auth.logout(request)
    messages.success(request, "Logout Successful")
    return redirect(home)

def login(request):
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)
        
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])
            if user:
                auth.login(user=user, request=request)
                return redirect(reverse('home'))
    else:
        form = UserLoginForm()
        return render(request, 'accounts/login.template.html', {
            'form':form
        })
