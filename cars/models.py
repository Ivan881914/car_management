from django.db import models
from django.contrib.auth.models import User

class Car(models.Model):
    make = models.CharField(max_length=100)  # Марка
    model = models.CharField(max_length=100)  # Модель
    year = models.PositiveIntegerField()  # Год выпуска
    description = models.TextField()  # Описание
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания
    updated_at = models.DateTimeField(auto_now=True)  # Дата обновления
    owner = models.ForeignKey(User, on_delete=models.CASCADE)  # Владелец

    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"

class Comment(models.Model):
    car = models.ForeignKey('Car', on_delete=models.CASCADE, related_name='comments')  # Связь с автомобилем
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Связь с пользователем
    content = models.TextField()  # Текст комментария
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания комментария

    def __str__(self):
        return f'Комментарий {self.author.username} к {self.car}'
