from django.contrib import admin
from .models import Category, Cupcake, Cookie, Bun, Cake, Product, CartItem, Delivery

admin.site.register(Category)
admin.site.register(Bun)
admin.site.register(Cookie)
admin.site.register(Cupcake)
admin.site.register(Cake)
admin.site.register(Product)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ['address', 'entrance', 'apartment', 'comm_for_order']
    filter_horizontal = ['cart_items']  # Удобный интерфейс для выбора позиций корзины

admin.site.register(CartItem)
admin.site.register(Delivery, DeliveryAdmin)