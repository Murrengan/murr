from PIL import Image
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager
from tinymce import HTMLField
from uuslug import slugify

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название категрии', help_text="Максимум 50 символов")
    slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField(verbose_name='Описание')
    m_title = models.CharField(max_length=60, verbose_name='Мета-тайтл', blank=True)

    class Meta:
        verbose_name='Категория'
        verbose_name_plural='Категории'

    def __str__(self):
        return self.name


class Murr(models.Model):

    CATEGORIES = [

        ('programming', '#программирование'),
        ('games', '#игры'),
        ('humor', '#смешное'),
        ('scince', '#наука'),
        ('sport', '#спорт'),
        ('cinema', '#кино'),
        ('music', '#музыка'),
        ('travels', '#путешествия'),
        ('relations', '#отношения'),
        ('etc', '#другое'),
    ]

    title = models.CharField(max_length=78, verbose_name='Заголовок', help_text="Максимум 78 символов")
    description = models.CharField(max_length=158, blank=True, verbose_name='Описание', help_text="Максимум 158 символа")
    content = HTMLField('Content')
    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='murrs')
    categories = models.CharField(max_length=20, verbose_name='Категория', choices=CATEGORIES)
    # category = models.ForeignKey(
    #     Category,
    #     verbose_name='Категория',
    #     related_name='murrs',
    #     on_delete=models.CASCADE,
    #     blank=True,
    #     null=True)

    featured = models.BooleanField(default=True)
    cover = models.ImageField(blank=True, upload_to='murren_pics')
    tags = TaggableManager(blank=True, verbose_name='Теги', help_text="Список тегов через запятую. Максимум 40 символов")
    slug = models.CharField(verbose_name='Слаг для мурра', max_length=100, blank=True)

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
    def comment_count(self):
        return Comment.objects.filter(murr=self).count()

    @property
    def cover_url(self):
        if self.cover and hasattr(self.cover, 'url'):
            return self.cover.url

    def get_liked_murrens(self):
        return self.liked.values_list('murren_id', flat=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.cover:
            img = Image.open(self.cover.path)

            if img:
                output_size = (1000, 1000)
                img.thumbnail(output_size)
                img.convert('RGB').save(self.cover.path, "JPEG")

        self.slug = f'{slugify(self.title)}-{self.pk}'
        super(Murr, self).save()


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    murr = models.ForeignKey(Murr, related_name='comments', on_delete=models.CASCADE)
    reply = models.ForeignKey(
        "self",
        verbose_name="Коммент",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='children',
    )

    def __str__(self):
        return f'<Comment: {self.murr.title}>'


class Like(models.Model):
    murren = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
    murr = models.ForeignKey(Murr, related_name='liked', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('murren', 'murr')

    def __str__(self):
        return f'{self.murren} liked {self.murr}'


class MurrAction(models.Model):
    REPORT = 'report'
    HIDE = 'hide'

    _ACTIONS_LIST = (
        (REPORT, 'Report Action'),
        (HIDE, 'Hide Action'),
    )

    kind = models.TextField(
        choices=_ACTIONS_LIST
    )
    murren = models.ForeignKey(
        User, models.CASCADE
    )
    timestamp = models.DateTimeField(
        auto_now_add=True
    )
    murr = models.ForeignKey(
        Murr,
        related_name='actions',
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ('murren', 'murr', 'kind', )
