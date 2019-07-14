from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Character(models.Model):
    name = models.CharField(max_length=25, verbose_name='Name', help_text="Имя", unique=True)
    actions = models.CharField(max_length=256, verbose_name='Actions', help_text="Действия")
    character_db = models.ForeignKey(User, on_delete=models.CASCADE, related_name='character_db', blank=True, null=True)
