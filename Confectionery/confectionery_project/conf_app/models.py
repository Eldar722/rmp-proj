from django.db import models
from pytils.translit import slugify
from datetime import datetime


class Category(models.Model):
    name = models.CharField("Название категории", max_length=255)
    image = models.ImageField("Изображение", upload_to="categories/images/", default="")
    slug = models.SlugField(unique=True, editable=False, blank=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Product(models.Model):
    title = models.CharField("Название", max_length=255)
    image = models.ImageField("Изображение", upload_to="products/images/", default="")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Выберите категорию")
    price = models.IntegerField("Цена")
    added_at = models.DateTimeField("Дата и время поступления", default=datetime.now)    

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.title
    
class Cookie(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, primary_key=True)
    
    class Meta:
        verbose_name = "Печенье"
        verbose_name_plural = "Печенья"

class Bun(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, primary_key=True)
    
    class Meta:
        verbose_name = "Булочка"
        verbose_name_plural = "Булочки"

class Cake(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, primary_key=True)
    
    class Meta:
        verbose_name = "Пирог"
        verbose_name_plural = "Пироги"

class Cupcake(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, primary_key=True)
    
    class Meta:
        verbose_name = "Капкейк"
        verbose_name_plural = "Капкейки"

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.product.price * self.quantity