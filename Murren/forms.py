from croppie.fields import CroppieField
from croppie.widgets import CroppieImageRatioWidget
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

User = get_user_model()


class MurrenCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ('username', 'email')


class MurrenChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('username', 'email')


class ProfileMurrenForm(forms.ModelForm):
    # set profile_picture to "not required" - allow change nick & e-mail w/o force image selection
    # profile_picture=forms.ImageField(required=False, widget=forms.FileInput(attrs={'class':'d-none'}))
    profile_picture = CroppieField(required=False,label="",
                                   widget=CroppieImageRatioWidget(
                                       options={
                                           'viewport': {
                                               'width': 200,
                                               'height': 200,
                                               'type': 'circle',
                                           },
                                           'showZoomer': True,
                                       },
                                       attrs={'class': 'd-none'}
                                   ))

    username = forms.CharField(widget=forms.TextInput({'class': 'form-control','placeholder': 'Изменить юзернейм'}),
                               label="юзернейм")
    email = forms.CharField(widget=forms.TextInput({'class': 'form-control', 'placeholder': 'Изменить почту'}),
                            label="Почта")

    class Meta:
        model = User
        fields = ('profile_picture', 'username', 'email')

# ========   advise from author of django-croppie   ========
# class MyForm(forms.Form):
#     image = CroppieField(
#         widget=CroppieImageRatioWidget(
#             attrs={
#                 'class': 'form-control', # any class you want here
#             }
#         ))
