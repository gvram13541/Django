from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomerRegistrationForm, CustomerLoginForm
from django.contrib.auth import authenticate, login as auth_login

def home(request):
    return render(request, 'customers/home.html')

def register(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Customer registered successfully!')
            return redirect('login')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CustomerRegistrationForm()
    return render(request, 'customers/register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = CustomerLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            role = form.cleaned_data.get('role')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                if user.role == role:
                    auth_login(request, user)
                    messages.success(request, 'Customer logged in successfully!')
                    if role == 'buyer':
                        return redirect('buyer_home')
                    else:
                        return redirect('seller_home')
                else:
                    messages.error(request, 'Invalid role')
            else:
                messages.error(request, 'Invalid email or password')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CustomerLoginForm()
    return render(request, 'customers/login.html', {'form': form})

# def login(request):
#     if request.method == 'POST':
#         form = CustomerLoginForm(request.POST)
#         if form.is_valid():
#             messages.success(request, 'Customer logged in successfully!')
#             return redirect('home')
#         else:
#             messages.error(request, 'Please correct the errors below.')
#     else:
#         form = CustomerLoginForm()
#     return render(request, 'customers/login.html', {'form': form})