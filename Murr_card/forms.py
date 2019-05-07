from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, HTML, Field
from django import forms
from django.utils.html import strip_tags
from tinymce import TinyMCE

from .models import Murr, Comment


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class CustomCheckbox(Field):
    template = 'Murr_card/custom_checkbox.html'


class MurrForm(forms.ModelForm):
    content = forms.CharField(
        widget=TinyMCEWidget(
            attrs={'required': False, 'cols': 30, 'rows': 10},
            mce_attrs=({'menubar': False,
                        'plugins': ['advlist autolink lists link image charmap print preview anchor textcolor',
                                    'searchreplace visualblocks code fullscreen',
                                    'insertdatetime media table contextmenu paste code help wordcount'],
                        'toolbar': '''
                                insert | undo redo |  formatselect | bold italic backcolor  | 
                                alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | 
                                removeformat | help',
                                ''',
                        'toolbar2': '''''',
                        'content_css': ['//fonts.googleapis.com/css?family=Lato:300,300i,400,400i',
                                        '//www.tinymce.com/css/codepen.min.css'],
                        'branding': False,
                        })
        )
    )

    class Meta:
        model = Murr
        fields = ('title', 'description', 'content', 'tags', 'categories', 'cover', 'is_draft', 'is_public')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('title', css_class='form-group col-md-4 mb-0'),
                Column('description', css_class='form-group col-md-8 mb-0'),
                css_class='form-row text-left mt-5'
            ),
            'content',
            Row(
                Column('tags', css_class='form-group col-12 mb-0'),
                Column('categories', css_class='form-group col-12 mb-0'),
                css_class='form-row text-left '
            ),
            Row(
                HTML('''
                <div class='border-right border-secondary col-6 form-group formColumn mb-0 offset-1'>
                    <input type="image" 
                        src="{{ form.instance.cover_url | default_if_none:"/static/img/NoImageAvailable.png" }}" 
                        data-toggle="tooltip" data-placement="top" title="Щелкните чтобы изменить" width="100px" 
                        height="100px" class="rounded bg-light" style="outline: none;" id="cover-img"/>
                </div> 
                '''),
                # <input type="file" name="file-3[]" id="file-3" class="inputfile inputfile-3">
                Column('cover', css_class='inputfile inputfile-3 d-none'),
                Column(CustomCheckbox('is_draft'),css_class='form-group mx-3 mb-0'),
                Column(CustomCheckbox('is_public'),css_class='form-group mx-3 mb-0'),
                css_class='form-row text-left align-items-md-center'
            ),
            HTML('<hr class="border-3 shadow-sm">'),
            Submit('submit', 'Сохранить', css_class='mt-3')
        )

    def clean_tags(self):
        """Cleaning tags from backslashes and strip html-tags"""

        tags = self.cleaned_data.get('tags')
        tags = [strip_tags(tag).replace('/', '') for tag in tags]
        return filter(bool, tags)


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control',
               'placeholder': 'введите ваш комментарий',
               'rows': '4', }
    ))

    class Meta:
        model = Comment
        fields = ('content',)


class CommentEditForm(forms.ModelForm):
    # reply = forms.IntegerField(
    #     # widget=forms.HiddenInput,
    #     required=False
    # )
    #
    # content = forms.CharField(
    #     label="Comment content",
    #     widget=forms.Textarea(
    #          attrs={'required': False, 'rows': 4, 'id':'comment-area', }
    #     ))
    content = forms.CharField(
        label="Comment content",
        widget=TinyMCEWidget(
             attrs={'required': False, 'rows': 4, 'id': 'comment-area', }
        ))

    class Meta:
        model = Comment
        fields = ('content', )
