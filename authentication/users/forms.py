# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
# from django import forms
# from .models import Profile


# class UserRegisterForm(UserCreationForm):
#     email = forms.EmailField()
#     phone_number = forms.CharField(max_length=15, required=True)

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'phone_number', 'password1', 'password2']
        

# class UserUpdateForm(forms.ModelForm):
#     email = forms.EmailField()
    
#     class Meta:
#         model = User
#         fields = ['username', 'email']
        

# class ProfileUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['image']
        
        
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=15, required=True, 
                                 help_text='Enter your phone number with country code (e.g., +91XXXXXXXXXX)')

    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

class OTPVerificationForm(forms.Form):
    otp = forms.CharField(
        label='Enter OTP',
        max_length=6,
        min_length=6,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter 6-digit OTP'
        })
    )