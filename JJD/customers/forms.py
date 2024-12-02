from django import forms
from django.contrib.auth import authenticate
from .models import Customer
from django.contrib.auth.hashers import make_password

class CustomerRegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}),
        label="Confirm Password"
    )
    
    class Meta:
        model = Customer
        fields = ['name', 'phone', 'email', 'village', 'district', 'state', 'country', 'pincode', 'role', 'password']
        widgets = {
            'role': forms.RadioSelect(choices=Customer.ROLE_CHOICES),
            'email': forms.EmailInput(),
            'pincode': forms.NumberInput(),
            'password': forms.PasswordInput(attrs={'placeholder': 'Enter Password'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        
        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', 'Passwords do not match.')
        return cleaned_data
    
    def save(self, commit=True):
        customer = super().save(commit=False)
        customer.password = make_password(self.cleaned_data['password'])
        if commit:
            customer.save()
        return customer


class CustomerLoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    role = forms.ChoiceField(widget=forms.RadioSelect, choices=Customer.ROLE_CHOICES, initial='buyer')

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        role = cleaned_data.get('role')
        
        if not email or not password:
            raise forms.ValidationError("Email and Password are required.")
        return cleaned_data

    def get_user(self):
        email = self.cleaned_data.get('email')
        return Customer.objects.get(email=email)


















# from django import forms
# from .models import Customer
# from django.contrib.auth.hashers import check_password, make_password

# class CustomerRegistrationForm(forms.ModelForm):
#     confirm_password = forms.CharField(
#         widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}),
#         label="Confirm Password"
#     )
    
#     class Meta:
#         model = Customer
#         fields = ['name', 'phone', 'email', 'village', 'district', 'state', 'country', 'pincode', 'seller', 'password']
#         widgets = {
#             'seller': forms.CheckboxInput(),
#             'email': forms.EmailInput(),
#             'pincode': forms.NumberInput(),
#             'password': forms.PasswordInput(attrs={'placeholder': 'Enter Password'}),
#         }

#     def clean(self):
#         cleaned_data = super().clean()
#         password = cleaned_data.get('password')
#         confirm_password = cleaned_data.get('confirm_password')
        
#         if password and confirm_password and password != confirm_password:
#             self.add_error('confirm_password', 'Passwords do not match.')
#         return cleaned_data
    
#     def save(self, commit=True):
#         customer = super().save(commit=False)
#         customer.password = make_password(self.cleaned_data['password'])
#         if commit:
#             customer.save()
#         return customer


# class CustomerLoginForm(forms.ModelForm):
#     class Meta:
#         model = Customer
#         fields = ['email', 'password']
#         widgets = {
#             'email': forms.EmailInput(),
#             'password': forms.PasswordInput(),
#         }

#     def clean(self):
#         cleaned_data = super().clean()
#         email = cleaned_data.get('email')
#         password = cleaned_data.get('password')
        
#         try:
#             customer = Customer.objects.get(email=email)
#             if not check_password(password, customer.password):
#                 self.add_error('password', 'Invalid password.')
#         except Customer.DoesNotExist:
#             self.add_error('email', 'Customer does not exist.')
#         return cleaned_data