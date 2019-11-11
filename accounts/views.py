from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import auth, messages
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

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
                return redirect(reverse('profile'))
    else:
        form = UserLoginForm()
        return render(request, 'accounts/login.template.html', {
            'form':form
        })

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "Welcome! Thank you for registering.")
            else:
                messages.error(request, "Unable to register at the moment. Please try again later.")
            return redirect(reverse('home'))
        else:
            return render(request, "accounts/register.template.html",{
                'form': form
            })
    else:
        register_form = UserRegistrationForm()
        return render(request, "accounts/register.template.html", {
            'form': register_form
        })

@login_required    
def profile(request):
    User = get_user_model()
    user = User.objects.get(email=request.user.email)
    return render(request, 'accounts/profile.template.html', {
        'user' : user
    })
