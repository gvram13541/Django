from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .serializers import CustomerRegistrationSerializer, CustomerLoginSerializer
from .models import Customer

@api_view(['GET'])
def home(request):
    return Response({"message": "Welcome to the home page!"})

@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        serializer = CustomerRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Customer registered successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        serializer = CustomerLoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            role = serializer.validated_data['role']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                if user.role == role:
                    token, created = Token.objects.get_or_create(user=user)
                    return Response({"message": "Customer logged in successfully!", "token": token.key}, status=status.HTTP_200_OK)
                return Response({"error": "Invalid role"}, status=status.HTTP_400_BAD_REQUEST)
            return Response({"error": "Invalid email or password"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def buyer_home(request):
    return Response({"message": "Welcome to the buyer home page!"})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def seller_home(request):
    return Response({"message": "Welcome to the seller home page!"})
































# from django.shortcuts import render, redirect
# from django.contrib import messages
# from .forms import CustomerRegistrationForm, CustomerLoginForm
# from django.contrib.auth import authenticate, login as auth_login
# from django.contrib.auth.decorators import login_required

# def home(request):
#     return render(request, 'customers/home.html')

# def register(request):
#     if request.method == 'POST':
#         form = CustomerRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Customer registered successfully!')
#             return redirect('login')
#         else:
#             messages.error(request, 'Please correct the errors below.')
#     else:
#         form = CustomerRegistrationForm()
#     return render(request, 'customers/register.html', {'form': form})

# def login(request):
#     if request.method == 'POST':
#         form = CustomerLoginForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data.get('email')
#             password = form.cleaned_data.get('password')
#             role = form.cleaned_data.get('role')
#             user = authenticate(request, email=email, password=password)
#             if user is not None:
#                 if user.role == role:
#                     auth_login(request, user)
#                     messages.success(request, 'Customer logged in successfully!')
#                     if role == 'buyer':
#                         return redirect('buyer_home')
#                     else:
#                         return redirect('seller_home')
#                 else:
#                     messages.error(request, 'Invalid role')
#             else:
#                 messages.error(request, 'Invalid email or password')
#         else:
#             messages.error(request, 'Please correct the errors below.')
#     else:
#         form = CustomerLoginForm()
#     return render(request, 'customers/login.html', {'form': form})

# @login_required
# def buyer_home(request):
#     return render(request, 'customers/buyer_home.html')

# @login_required
# def seller_home(request):
#     return render(request, 'customers/seller_home.html')

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