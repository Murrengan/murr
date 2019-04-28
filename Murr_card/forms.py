from tinymce import TinyMCE

from django import forms
from django.utils.html import strip_tags

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
        fields = ('title', 'description', 'content', 'tags', 'categories', 'cover', 'is_draft', 'is_public')
        # TODO - Надо-бы офрмить виджеты стильно (но с тем что ниже, пока не получилось)
        # (возможно Crispy Form перекрывает что то в классах)
        # widgets={'is_draft': forms.CheckboxInput(attrs={'class':'custom-control-input'}),
        #          'is_public': forms.CheckboxInput(attrs={'class':'custom-control-input'}),}

    def clean_tags(self):
        """Cleaning tags from backslashes and strip html-tags"""

        tags = self.cleaned_data.get('tags')
        tags = [strip_tags(tag).replace('/', '') for tag in tags]
        return filter(bool, tags)


class CommentForm(forms.ModelForm):

    content = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control',
        'placeholder': 'введите ваш комментарий',
        'rows': '4',}

    ))

    class Meta:
        model = Comment
        fields = ('content',)


class CommentEditForm(forms.Form):

    parent_comment = forms.IntegerField(
        # widget=forms.HiddenInput,
        required=False
    )

    comment_area = forms.CharField(
        label="",
        widget=TinyMCEWidget(
            attrs={'required': False, 'rows': 4}
        )
    )
