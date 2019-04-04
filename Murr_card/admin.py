from django.contrib import admin

from .models import Murr, Category, Author, Comment, MurrView

admin.site.register(Murr)
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Comment)
admin.site.register(MurrView)
