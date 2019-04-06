from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from tinymce import HTMLField

User = get_user_model()


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(default='default_murren_img.jpg', upload_to='murren_pics')

    def __str__(self):
        return self.user.username


class Category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Murr(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=78, blank=True)
    content = HTMLField('Content')
    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, blank=True)
    featured = models.BooleanField(default=True)
    cover = models.ImageField(blank=True, upload_to='murren_pics')
    is_draft = models.BooleanField("Черновик",
                                   default=False,
                                   blank=True,
                                   help_text="Черновики не публикуются")
    is_public = models.BooleanField("Общедоступен",
                                    default=True,
                                    blank=True,
                                    help_text="Murr общедоступен или только для авторизованным пользователям")

    def __str__(self):
        return self.title

    def get_update_url(self):
        return reverse('murr_update', kwargs={
            'pk': self.id
        })

    def get_delete_url(self):
        return reverse('murr_delete', kwargs={
            'pk': self.id
        })

    # возвращает все комментарии к конкретному мурру,
    # так как в можеле Comment стоит related_name='comments'
    # и прописано return self.comments.all()
    @property
    def get_comments(self):
        return self.comments.all().order_by('-timestamp')

    @property
    def view_count(self):
        return MurrView.objects.filter(murr=self).count()

    @property
    def comment_count(self):
        return Comment.objects.filter(murr=self).count()


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    murr = models.ForeignKey(Murr, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class MurrView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    murr = models.ForeignKey(Murr, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
