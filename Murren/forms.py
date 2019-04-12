from allauth.account.forms import SignupForm
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

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



class CustomSignupForm(SignupForm):
    field_order = ['murren_name', 'password', 'email']

    murren_name = forms.CharField(max_length=30, label='Имя Murrenа',
                                  widget=forms.TextInput(attrs={
                                      'placeholder': 'Your_MURR_Name'
                                  }))
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'type': 'email',
               'placeholder': 'Электронная почта'}))

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.murren_name = self.cleaned_data['murren_name']
        user.save()
        return user

    class Meta:
        model = User
        fields = ('password','email','murren_name')
