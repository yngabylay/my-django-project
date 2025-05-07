# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Table
from .forms import RegisterForm, ReservationForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')  # Перенаправление на страницу логина после успешной регистрации

def home(request):
    return render(request, 'home.html')  # Отображение главной страницы ресторана

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'registration/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user:
            login(request, user)
            return redirect('restaurant_home')  # Перенаправление на главную страницу ресторана
        else:
            messages.error(request, "Неверный логин или пароль")
    return render(request, 'registration/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def restaurant_home(request):
    return render(request, 'restaurant_home.html')

@login_required
def profile(request):
    return render(request, 'profile.html')

@login_required
def book_table(request):
    # Если это POST-запрос, значит пользователь отправил форму бронирования
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            # Сохраняем форму, связываем с текущим пользователем
            reservation = form.save(commit=False)
            reservation.user = request.user  # Привязываем бронь к текущему пользователю
            reservation.save()
            return redirect('home')  # После успешного бронирования редиректим на главную страницу
    else:
        form = ReservationForm()  # Если GET-запрос, создаем пустую форму

    return render(request, 'book_table.html', {'form': form})  # Отправляем форму на страницу

def restaurant_home(request):
    return render(request, 'restaurant_home.html') 