from django.contrib.auth.models import AbstractUser
from django.db import models


# Создается когда клиент регистрируется
class CustomMurren(AbstractUser):
    profile_picture = models.ImageField(default='default_murren_img.jpg', upload_to='murren_pics', verbose_name='Пикча')
    murren_name = models.CharField(max_length=30, blank=True, default='молочко', verbose_name='Ник Муррена')

    def __str__(self):
        return self.email

