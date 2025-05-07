from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Reservation

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# Форма бронирования столика
class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['table_number', 'reservation_time', 'special_requests']