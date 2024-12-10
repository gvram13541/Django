from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import CustomerRegistrationForm, CustomerLoginForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from .models import Product, Order

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

@login_required
def buyer_home(request):
    products = Product.objects.all()
    return render(request, 'customers/buyer_home.html', {'products': products})

@login_required
def seller_home(request):
    return render(request, 'customers/seller_home.html')


@login_required
def product_detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'customers/product_detail.html', {'product': product})

@login_required
def add_to_cart(request, id):
    product = get_object_or_404(Product, id=id)
    cart = request.session.get('cart', {})
    if str(id) in cart:
        cart[str(id)] += 1
    else:
        cart[str(id)] = 1
    request.session['cart'] = cart
    messages.success(request, 'Product added to cart successfully!')
    return redirect('buyer_home')

@login_required
def remove_from_cart(request, id):
    product = get_object_or_404(Product, id=id)
    cart = request.session.get('cart', {})
    if str(id) in cart:
        cart[str(id)] -= 1
        if cart[str(id)] == 0:
            cart.pop(str(id))
    request.session['cart'] = cart
    messages.success(request, 'Product removed from cart successfully!')
    return redirect('buyer_home')

@login_required
def view_cart(request):
    cart = request.session.get('cart', {})
    products = Product.objects.filter(id__in=cart.keys())
    return render(request, 'customers/view_cart.html', {'products': products})

@login_required
def place_order(request):
    if request.method == 'POST':
        selected_product = Product.objects.get(id=request.POST['product_id'])
        selected_quantity = float(request.POST['quantity'])
        
        order = Order.objects.create(
            customer=request.user.customer,
            product=selected_product,
            quantity=selected_quantity,
            status=False  
        )
        
        request.session['order_id'] = order.id
        return redirect('order_confirmed')
    else:
        products = Product.objects.all()
        return render(request, 'customers/order_placed.html', {'products': products})

@login_required
def order_summary(request):
    orders = Order.objects.filter(customer=request.user, status=False)  # status should be a boolean
    total_cost = sum(order.product.price * order.quantity for order in orders)
    return render(request, 'customers/order_summary.html', {'orders': orders, 'total_cost': total_cost})

@login_required
def order_confirmed(request):
    try:
        order_id = request.session.get('order_id')
        if order_id:
            order = Order.objects.get(id=order_id)
            order.status = True  # Set status to True to mark as confirmed
            order.save()
            return render(request, 'customers/order_confirmed.html')
        else:
            return redirect('buyer_home')
    except Order.DoesNotExist:
        return redirect('buyer_home')
    

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