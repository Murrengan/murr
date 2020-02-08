from django.contrib.auth import get_user_model
from django.db import models


Murren = get_user_model()


class MurrCard(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
    timestamp = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(Murren, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
