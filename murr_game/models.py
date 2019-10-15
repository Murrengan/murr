from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class MurrenGameData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='murren_game_data')
    hp = models.IntegerField(default=60)
    mp = models.IntegerField(default=20)
    lvl = models.IntegerField(default=1)
    exp = models.IntegerField(default=0)
    locations = models.CharField(max_length=255)

    strength = models.IntegerField(default=5)
    vitality = models.IntegerField(default=5)
    dexterity = models.IntegerField(default=5)
    intelligence = models.IntegerField(default=5)
    luck = models.IntegerField(default=1)

    inventory = models.ManyToManyField('Inventory')
    skill = models.ManyToManyField('Skill')
    armory = models.ManyToManyField('Armory')


class Inventory(models.Model):
    name = models.CharField(max_length=30)
    value = models.IntegerField(default=0)
    description = models.CharField(max_length=255)


class Skill(models.Model):
    name = models.CharField(max_length=30)
    mp_value = models.IntegerField(default=0)
    description = models.CharField(max_length=255)


class Armory(models.Model):
    name = models.CharField(max_length=30)
    attack = models.IntegerField(default=0)
    defence = models.IntegerField(default=0)
    buff = models.IntegerField(default=0, help_text='Изменяет базовые характеристики')
    description = models.CharField(max_length=255)
