from django.contrib import admin

from .models import Murr, Comment, Category

admin.site.register(Murr)
admin.site.register(Comment)

@admin.register(Category)
class  CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
