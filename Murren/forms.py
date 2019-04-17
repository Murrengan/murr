from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
import re
from django.utils.safestring import SafeText
User = get_user_model()


class CustomMurrenCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ('username', 'email')


class CustomMurrenChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('username', 'email')


class ProfileMurrenForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('profile_picture', 'murren_name', 'email')

    def __str__(self):
        string = super().__str__()
        ind = re.search(r"Изменить", string)
        return SafeText(string[ind.start():])