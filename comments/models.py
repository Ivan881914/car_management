from django.db import models
from django.contrib.auth.models import User
from cars.models import Car

class Comment(models.Model):
    content = models.TextField()  # Текст комментария
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания
    car = models.ForeignKey(Car, related_name='comments', on_delete=models.CASCADE)  # Связь с автомобилем
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Автор комментария

    def __str__(self):
        return f"Comment by {self.author} on {self.car}"
