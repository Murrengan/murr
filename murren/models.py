from django.contrib.auth.models import AbstractUser
from django.db import models


class Murren(AbstractUser):

    email = models.EmailField()

    def __str__(self):
        return self.username
