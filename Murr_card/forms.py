from django import forms
# from django.forms import CheckboxInput

from tinymce import TinyMCE

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
        # TODO - Надо-бы офрмить виджеты стильно (но с тем что ниже, пока не получилось)
        #
        # widgets={'is_draft': forms.CheckboxInput(attrs={'class':'custom-control-input'}),
        #          'is_public': forms.CheckboxInput(attrs={'class':'custom-control-input'}),}


class CommentForm(forms.ModelForm):

    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'введите ваш комментарий',
        'rows': '4',

    }))

    class Meta:
        model = Comment
        fields = ('content', )
