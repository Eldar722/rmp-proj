from django.contrib import admin
from .models import Category, Cupcake, Cookie, Bun, Cake, Product, CartItem

admin.site.register(Category)
admin.site.register(Bun)
admin.site.register(Cookie)
admin.site.register(Cupcake)
admin.site.register(Cake)
admin.site.register(Product)
admin.site.register(CartItem)