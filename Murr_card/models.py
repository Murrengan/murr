from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import reverse
from django.utils import timezone


class Category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Murr(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_count = models.IntegerField(default=0)
    categories = models.ManyToManyField(Category)
    featured = models.BooleanField()
    slag = models.SlugField(max_length=128, unique=True)
    image = models.ImageField(default='default_murren_img.jpg', upload_to='murren_pics')

    # позволяет в HTML шаблоне обрашаться к murr_detail по штуке {{ murr.get_absolute_url }}
    def get_absolute_url(self):
        context = {
            'slag': self.slag
        }
        return reverse('murr_detail', kwargs=context)

    def __str__(self):
        return self.title
