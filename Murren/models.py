from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomMurren(AbstractUser):

    def __str__(self):
        return self.email


class MurrenProfile(models.Model):
    user = models.OneToOneField(CustomMurren, on_delete=models.CASCADE)
    profile_picture = models.ImageField(default='default_murren_img.jpg', upload_to='murren_pics')
    murren_name = models.CharField(max_length=30, blank=True, default='молочко')

    def __str__(self):
        return self.user.username
