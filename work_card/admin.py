from django.contrib import admin

from .models import WorkCard, Rubric


class WorkCardAdmin(admin.ModelAdmin):
    list_display = ('title', 'rubric')
    list_display_links = ('title', 'rubric')
    # по каким полям идет поиск
    search_fields = ('city', 'title', 'contact')


admin.site.register(WorkCard, WorkCardAdmin)
admin.site.register(Rubric)
