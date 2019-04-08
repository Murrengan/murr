from django.contrib import admin

from .models import Murr, Category, Comment, MurrView

admin.site.register(Murr)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(MurrView)
