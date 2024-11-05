from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Delivery

class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "password1", "password2")

class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = ['address', 'entrance', 'apartment', 'comm_for_order']
        labels = {
            'address': 'Адрес доставки',
            'entrance': 'Подъезд',
            'apartment': 'Квартира',
            'comm_for_order': 'Комментарий к заказу',
        }