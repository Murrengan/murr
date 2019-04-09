from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomMurrenCreationForm, CustomMurrenChangeForm
from .models import CustomMurren


class CustomUserAdmin(UserAdmin):
    add_form = CustomMurrenCreationForm
    form = CustomMurrenChangeForm
    model = CustomMurren
    list_display = ['email', 'username']


admin.site.register(CustomMurren, CustomUserAdmin)
