from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    title = models.CharField(max_length=255)  # Название задачи
    description = models.TextField(blank=True, null=True)  # Описание
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания

    def __str__(self):
        return self.title


class Table(models.Model):
    number = models.PositiveIntegerField(unique=True)
    is_reserved = models.BooleanField(default=False)
    reserved_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"Столик {self.number} - {'Занят' if self.is_reserved else 'Свободен'}"
    
class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table_number = models.IntegerField()
    reservation_time = models.DateTimeField()
    special_requests = models.TextField(blank=True)

    def __str__(self):
        return f"Table {self.table_number} reservation by {self.user.username} at {self.reservation_time}"

