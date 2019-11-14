from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import auth, messages
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth import get_user_model, update_session_auth_hash
from django.contrib.auth.decorators import login_required

# Create your views here.
def logout(request):
    auth.logout(request)
    messages.success(request, "Logout Successful")
    return render(request, 'shop/home.template.html')

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
            return render(request, 'shop/home.template.html')
        else:
            return render(request, "accounts/register.template.html",{
                'form': form
            })
    else:
        register_form = UserRegistrationForm()
        return render(request, "accounts/register.template.html", {
            'form': register_form
        })

def editProfile(request):
    User = get_user_model()
    user = User.objects.get(email=request.user.email)
    form = UserRegistrationForm(instance=user)

    if request.method == "POST":
        form = UserRegistrationForm(request.POST, request.FILES, instance=user)
        
        if form.is_valid():
            update = form.save(commit=False)               
            update.user = user
            update.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Profile Updated")
            return redirect(reverse('home'))                

    else:
        form = UserRegistrationForm(instance=user)
        return render(request, 'accounts/edit_profile.template.html', {'form': form})
        
@login_required    
def profile(request):
    User = get_user_model()
    user = User.objects.get(email=request.user.email)
    return render(request, 'accounts/profile.template.html', {
        'user' : user
    })

