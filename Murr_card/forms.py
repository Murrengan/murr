from django import forms
from tinymce import TinyMCE
from allauth.account.forms import ResetPasswordForm
from django.utils.translation import ugettext_lazy as _

from .models import Murr, Comment


class TinyMCEWidget(TinyMCE):
    
    def use_required_attribute(self, *args):
        return False


class MurrForm(forms.ModelForm):
    content = forms.CharField(
        widget=TinyMCEWidget(
            attrs={'required': False, 'cols': 30, 'rows': 10}
        )
    )

    class Meta:
        model = Murr
        fields = ('title', 'description', 'content', 'categories', 'cover', 'is_draft', 'is_public')


class CommentForm(forms.ModelForm):

    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'введите ваш комментарий',
        'rows': '4',

    }))

    class Meta:
        model = Comment
        fields = ('content', )


class MyCustomSetPasswordForm(ResetPasswordForm):

    email = forms.EmailField(
        label=_("ДЬКДЬВКПДЛВТПК"),
        required=True,
        widget=forms.TextInput(attrs={
            "type": "email",
            "size": "30",
            "placeholder": _("ОТАПУОТПУЫП"),
        })
    )