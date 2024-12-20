from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Bun, Cookie, Cake, Cupcake, Product, CartItem, Delivery
from .forms import DeliveryForm
from django import forms
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import NewUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse


def home_page(request):
    categories = Category.objects.all()
    products = Product.objects.all().order_by('-added_at')[:10]
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
        'product_title': product.title,
        'product_price': product.price,
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
    print(f"Запрос на уменьшение количества для элемента с ID: {cart_item_id}")
    
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    print(f"Найден элемент корзины: {cart_item}")

    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
        print(f"Количество уменьшено. Новое количество: {cart_item.quantity}")
    else:
        cart_item.delete()
        print(f"Элемент корзины удалён, так как его количество достигло 0.")

    return redirect('view_cart')

# def delivery(request):
#     if request.method == 'POST':
#         form = DeliveryForm(request.POST)
#         if form.is_valid():
#             form.save()  # Сохранение данных в БД
#             return redirect('success_page')
            
#     else:
#         form = DeliveryForm()

    
#     return render(request, './delivery.html', {'form': form})

def delivery(request):
    cart_items = CartItem.objects.all()
    total_sum = sum(item.total_price() for item in cart_items)

    if request.method == 'POST':
        form = DeliveryForm(request.POST)
        if form.is_valid():
            form.save()  # Сохранение данных в БД
            return redirect('success_page')
    else:
        form = DeliveryForm()

    return render(request, './delivery.html', {
        'form': form,
        'total_sum': total_sum,
    })

def success_page(request):
    return render(request, './success.html') 

def complete_order(request):
    # Получаем все позиции корзины пользователя
    cart_items = CartItem.objects.filter(user=request.user)
    if not cart_items:
        return JsonResponse({'error': 'Корзина пуста.'}, status=400)

    # Создаем новый объект Delivery и связываем его с позициями корзины
    delivery = Delivery.objects.create(
        address="Адрес клиента",
        entrance="Подъезд клиента",
        apartment="Квартира клиента",
        comm_for_order="Комментарий клиента"
    )
    
    # Связываем все позиции корзины с созданной доставкой
    delivery.cart_items.set(cart_items)
    delivery.save()

    # После оформления заказа очищаем корзину
    cart_items.delete()

    return JsonResponse({'success': 'Заказ оформлен и доставка создана.'})