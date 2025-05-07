
from django.contrib import admin
from django.urls import path, include
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # Стандартные URL для логина
    path('accounts/signup/', views.SignUpView.as_view(), name='signup'),  # Класс для регистрации
    path('restaurant_home/', views.restaurant_home, name='restaurant_home'),  # Маршрут для страницы ресторана
    path('', views.home, name='home'),  # Главная страница
    path('profile/', views.profile, name='profile'),
    path('book_table/', views.book_table, name='book_table'),
    path('logout/', views.logout_view, name='logout'),
]
