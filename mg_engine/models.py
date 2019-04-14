from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Blockman(models.Model):
    name = models.CharField(max_length=50, default='Blockman_base')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blockman')
    maxhp = models.PositiveIntegerField(default=100)
    hp = models.PositiveIntegerField(default=100)
    power = models.PositiveIntegerField(default=20)

    def __str__(self):
        return self.name
