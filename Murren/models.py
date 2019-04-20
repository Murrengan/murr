from PIL import Image
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomMurren(AbstractUser):
    profile_picture = models.ImageField(default='default_murren_img.jpg', upload_to='murren_pics', verbose_name='Пикча')

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.profile_picture.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.profile_picture.path)
