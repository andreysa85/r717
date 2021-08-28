from django import forms
from .models import Order
from django.core.validators import RegexValidator

class OrderCreateForm(forms.ModelForm):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Формат для телефону: '+380000000'.")
    phone = forms.CharField(validators=[phone_regex], max_length=15)
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'phone',]