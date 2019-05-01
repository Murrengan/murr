from PIL import Image
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Q
from django.urls import reverse
from taggit.managers import TaggableManager
from tinymce import HTMLField
from uuslug import slugify

User = get_user_model()


class Category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class MurrManager(models.Manager):

    def get_visible(self, user_id=None):
        """ Return all non-private murrs and user's drafts (if user_id passed) """
        if user_id is None:
            return self.filter(is_public=True, is_draft=False)

        is_visible = Q(is_draft=True, author_id=user_id) | Q(is_draft=False)
        return self.filter(is_visible)


class Murr(models.Model):
    title = models.CharField(max_length=78, verbose_name='Заголовок')
    description = models.CharField(max_length=158, blank=True, verbose_name='Описание')
    content = HTMLField('Content')
    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='murrs')
    categories = models.ManyToManyField(Category, blank=True, related_name='murrs')
    featured = models.BooleanField(default=True)
    cover = models.ImageField(blank=True, upload_to='murren_pics')
    is_draft = models.BooleanField("Черновик", default=False, blank=True)
    is_public = models.BooleanField("Общедоступен", default=True, blank=True)
    tags = TaggableManager(blank=True, help_text="Список тегов через запятую")
    slug = models.CharField(verbose_name='Слаг для мурра', max_length=100, blank=True)

    objects = MurrManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('murr_detail', kwargs={'pk': self.id})

    def get_update_url(self):
        return reverse('murr_update', kwargs={'pk': self.id})

    def get_delete_url(self):
        return reverse('murr_delete', kwargs={'pk': self.id})

    @property
    def get_comments(self):
        return self.comments.order_by('-timestamp')

    @property
    def view_count(self):
        return MurrVisiting.objects.filter(murr=self).count()

    @property
    def comment_count(self):
        return Comment.objects.filter(murr=self).count()

    def murrs_count(self, **kwargs):
        return self.objects.filter(author=kwargs.get('author')).count()

    @property
    def cover_url(self):
        if self.cover and hasattr(self.cover, 'url'):
            return self.cover.url

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.cover:
            img = Image.open(self.cover.path)

            if img.height > 1000 or img.width > 1000:
                output_size = (1000, 1000)
                img.thumbnail(output_size)
                img.save(self.cover.path)

        self.slug = f'{slugify(self.title)}-{self.pk}'
        super(Murr, self).save()


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    murr = models.ForeignKey(
        Murr,
        related_name='comments',
        on_delete=models.CASCADE
    )
    reply = models.ForeignKey(
        "self",
        verbose_name="Коммент",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='children',
    )

    def __str__(self):
        return self.user.username
