from django import forms
from tinymce import TinyMCE

from .models import Murr


class TinyMCEWidget(TinyMCE):
    
    def use_required_attribute(self, *args):
        return False


class PostForm(forms.ModelForm):
    content = forms.CharField(
        widget=TinyMCEWidget(
            attrs={'required': False, 'cols': 30, 'rows': 10}
        )
    )

    class Meta:
        model = Murr
        fields = '__all__'
