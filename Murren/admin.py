from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import MurrenCreationForm, MurrenChangeForm
from .models import Murren


class CustomUserAdmin(UserAdmin):
    add_form = MurrenCreationForm
    form = MurrenChangeForm
    model = Murren

    list_display = ['email', 'username']



admin.site.register(Murren, CustomUserAdmin)
