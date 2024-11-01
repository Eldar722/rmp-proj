from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('categories/', views.menu_page, name='menu_page'),
    path('category/<slug:slug>/', views.category_page, name='category_page'),
    path('cart/', views.view_cart, name='view_cart'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('increase-quantity/<int:cart_item_id>/', views.increase_quantity, name='increase_quantity'),
    path('decrease-quantity/<int:cart_item_id>/', views.decrease_quantity, name='decrease_quantity'),
    path('sign-up/', views.sign_up_page, name='sign_up_page'),
    path('login/', views.login_page, name='login_page'),
    path('logout/', views.logout_action, name='logout_action')
]