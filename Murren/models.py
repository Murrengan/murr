from PIL import Image

from django.contrib.auth.models import AbstractUser
from django.db import models


class Murren(AbstractUser):
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


class Follower(models.Model):
    follower = models.ForeignKey(Murren, related_name='following', on_delete=models.CASCADE)
    following = models.ForeignKey(Murren, related_name='followers', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('follower', 'following')

    def __str__(self):
        return f'{self.follower} follows {self.following}'
