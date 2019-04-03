from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomMurren


class CustomMurrenCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomMurren
        fields = ('username', 'email')


class CustomMurrenChangeForm(UserChangeForm):

    class Meta:
        model = CustomMurren
        fields = ('username', 'email')


# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
#
#
# class MurrenRegisterForm(UserCreationForm):
#     email = forms.EmailField()
#
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']
