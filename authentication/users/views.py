# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from .forms import (
#     UserRegisterForm, 
#     UserUpdateForm, 
#     ProfileUpdateForm,
# )


# def home(request):
#     return render(request, 'users/home.html')


# def register(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     else:
#         form = UserRegisterForm()
#     return render(request, 'users/register.html', {'form':form})


# @login_required
# def profile(request):
#     if request.method == 'POST':
#         u_form = UserUpdateForm(
#             request.POST, 
#             instance=request.user
#         )
#         p_form = ProfileUpdateForm(
#             request.POST, 
#             request.FILES, 
#             instance=request.user.profile
#         )
#         if u_form.is_valid() and p_form.is_valid():
#             u_form.save()
#             p_form.save()
#             return redirect('profile')
#     else:
#         u_form = UserUpdateForm(instance=request.user)
#         p_form = ProfileUpdateForm(instance=request.user.profile)
        
#     context = {
#         'u_form': u_form,
#         'p_form': p_form,
#     }
    
#     return render(request, 'users/profile.html')







## to test wheather the email is working or not
# from django.core.mail import send_mail
# from django.http import HttpResponse
# def test_email(request):
#     send_mail(
#         'Test Email',
#         'This is a test email.',
#         'guna955reddy@gmail.com',
#         ['gunavardhan240@gmail.com'],
#         fail_silently=False,
#     )
#     return HttpResponse("Email sent!")



from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .utils import send_otp
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, OTPVerificationForm, LoginForm
from django.utils import timezone
from datetime import timedelta


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            try:
                user = User.objects.get(username=username)
                if user.check_password(password):
                    # Generate and send OTP
                    otp = user.profile.generate_otp()
                    if send_otp(user.profile.phone_number, otp):
                        request.session['login_user_id'] = user.id
                        messages.success(request, 'OTP has been sent to your registered mobile number.')
                        return redirect('verify_otp')
                    else:
                        messages.error(request, 'Error sending OTP. Please try again.')
                else:
                    messages.error(request, 'Invalid credentials')
            except User.DoesNotExist:
                messages.error(request, 'Invalid credentials')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})

def home(request):
    return render(request, 'users/home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            phone_number = form.cleaned_data.get('phone_number')
            user.profile.phone_number = phone_number
            user.profile.save()
            messages.success(request, 'Account created successfully! Please login.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def verify_otp(request):
    user_id = request.session.get('login_user_id')
    if not user_id:
        return redirect('login')

    otp = None
    otp_expiration_time = None

    if request.method == 'POST':
        form = OTPVerificationForm(request.POST)
        if form.is_valid():
            otp = form.cleaned_data.get('otp')
            try:
                user = User.objects.get(id=user_id)
                if user.profile.otp_generated_at is None:
                    messages.error(request, 'OTP has not been generated')
                    return redirect('login')
                
                otp_age = timezone.now() - user.profile.otp_generated_at
                if otp_age > timedelta(minutes=2):  # OTP expires after 2 minutes
                    messages.error(request, 'OTP has expired')
                    return redirect('login')
                
                if user.profile.otp == otp:
                    user.profile.is_verified = True
                    user.profile.otp = None  # Clear OTP after verification
                    user.profile.otp_generated_at = None  # Clear OTP timestamp
                    user.profile.save()
                    login(request, user)
                    del request.session['login_user_id']  # Clear session
                    messages.success(request, 'Login successful!')
                    return redirect('profile')
                else:
                    messages.error(request, 'Invalid OTP')
            except User.DoesNotExist:
                messages.error(request, 'Invalid user')
                return redirect('login')
    else:
        form = OTPVerificationForm()
        try:
            user = User.objects.get(id=user_id)
            otp = user.profile.otp
            if user.profile.otp_generated_at:
                otp_expiration_time = user.profile.otp_generated_at + timedelta(minutes=2)  # Calculate expiration time
                otp_expiration_time = otp_expiration_time.strftime('%Y-%m-%d %H:%M:%S')  # Format expiration time
        except User.DoesNotExist:
            otp = None

    return render(request, 'users/verify_otp.html', {'form': form, 'otp': otp, 'otp_expiration_time': otp_expiration_time})


# def verify_otp(request):
#     user_id = request.session.get('login_user_id')
#     if not user_id:
#         return redirect('login')
    
#     if request.method == 'POST':
#         form = OTPVerificationForm(request.POST)
#         if form.is_valid():
#             otp = form.cleaned_data.get('otp')
#             try:
#                 user = User.objects.get(id=user_id)
#                 if user.profile.otp == otp:
#                     user.profile.is_verified = True
#                     user.profile.otp = None  # Clear OTP after verification
#                     user.profile.save()
#                     login(request, user)
#                     del request.session['login_user_id']  # Clear session
#                     messages.success(request, 'Login successful!')
#                     return redirect('profile')
#                 else:
#                     messages.error(request, 'Invalid OTP')
#             except User.DoesNotExist:
#                 messages.error(request, 'Invalid user')
#                 return redirect('login')
#     else:
#         form = OTPVerificationForm()
#     return render(request, 'users/verify_otp.html', {'form': form})

@login_required
def profile(request):
    if not request.user.profile.is_verified:
        return redirect('login')
        
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, 
            request.FILES, 
            instance=request.user.profile
        )
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        
    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    
    return render(request, 'users/profile.html', context)