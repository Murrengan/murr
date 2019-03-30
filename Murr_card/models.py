from django.contrib.auth import get_user_model
from django.db import models
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
    comment_count = models.IntegerField(default=0)
    categories = models.ManyToManyField(Category)
    featured = models.BooleanField()
    cover = models.ImageField(blank=True, upload_to='murren_pics')

    def __str__(self):
        return self.title

    # возвращает все комментарии к конкретному мурру,
    # так как в можеле Comment стоит related_name='comments'
    # и прописано return self.comments.all()
    @property
    def get_comments(self):
        return self.comments.all().order_by('-timestamp')


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    post = models.ForeignKey(Murr, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
