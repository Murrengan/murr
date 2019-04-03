from django.contrib.auth.models import AbstractUser


class CustomMurren(AbstractUser):

    def __str__(self):
        return self.email
