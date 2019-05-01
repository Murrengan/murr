from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import FileInput, HiddenInput

from .models import Follower

User = get_user_model()


class MurrenFollower(forms.ModelForm):
    class Meta:
        model = Follower
        fields = ('follower', 'following')

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data


class MurrenCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ('username', 'email')


class MurrenChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('username', 'email')


class ProfileMurrenForm(forms.ModelForm):
    profile_picture=forms.ImageField(required=False, widget=forms.FileInput(attrs={'class':'d-none'}))
    # set profile_picture to "not required" - allow change nick & e-mail w/o force image selection

    class Meta:
        model = User
        fields = ('profile_picture', 'username', 'email')
        # widgets = {'profile_picture': forms.FileInput(attrs={'class': 'd-none'})}
