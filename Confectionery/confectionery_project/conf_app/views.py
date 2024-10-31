from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Bun, Cookie, Cake, Cupcake, Product, CartItem
from django.contrib.auth import login, authenticate, logout
from .forms import NewUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse


def home_page(request):
    categories = Category.objects.all()
    products = Product.objects.all().order_by('-added_at')[:6]
    context = {
        'categories': categories,  
        'products': products

    }

    return render (request, "./home.html", context)

def menu_page(request):
    categories = Category.objects.all()

    context = {
        'categories': categories,  
    }

    return render (request, "./menu.html", context)

def category_page(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category).order_by('-added_at')
    
    context = {
        'category': category,
        'products': products,
    }
    return render(request, "./categories/category_page.html", context)

def sign_up_page(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login_page')
        
    else:
        form = NewUserForm()
    context = {
        'form': form
    }
    return render (request, "./sign-up.html", context)

def login_page(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home_page')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, "./login.html", context)

def logout_action(request):
    logout(request)
    return redirect('home_page')

def view_cart(request):
    cart_items = CartItem.objects.all()
    total_sum = sum(item.total_price() for item in cart_items)
    return render(request, 'cart/cart.html', {'cart_items': cart_items, 'total_sum': total_sum})

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(product=product)
    if not created:
        cart_item.quantity += 1
    cart_item.save()

    total_sum = sum(item.total_price() for item in CartItem.objects.all())
    
    return JsonResponse({
        'product_name': product.name,
        'product_price': float(product.price),
        'quantity': cart_item.quantity,
        'total_sum': total_sum
    })

def update_cart_item(request, product_id, action):
    cart_item = get_object_or_404(CartItem, product__id=product_id)
    if action == 'increase':
        cart_item.quantity += 1
    elif action == 'decrease' and cart_item.quantity > 1:
        cart_item.quantity -= 1
    cart_item.save()

    total_sum = sum(item.total_price() for item in CartItem.objects.all())
    
    return JsonResponse({
        'quantity': cart_item.quantity,
        'total_sum': total_sum
    })

def increase_quantity(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    cart_item.quantity += 1
    cart_item.save()
    total_sum = sum(item.total_price() for item in CartItem.objects.all())
    
    return JsonResponse({'quantity': cart_item.quantity, 'total_sum': total_sum})

def decrease_quantity(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
    else:
        cart_item.delete()  # Удаляем товар, если количество 0
    total_sum = sum(item.total_price() for item in CartItem.objects.all())
    
    return JsonResponse({'quantity': cart_item.quantity if cart_item.id else 0, 'total_sum': total_sum})


