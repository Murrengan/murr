import bleach
from captcha.fields import ReCaptchaField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, HTML, Field
from django import forms
from django.conf import settings
from tinymce import TinyMCE

from .models import Murr, Comment


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class CustomCheckbox(Field):
    template = 'MurrCard/custom_checkbox.html'


class MurrForm(forms.ModelForm):

    LIMIT_LEN_TAGS = 40
    captcha = ReCaptchaField(
                             public_key=settings.RECAPTCHA_PUBLIC_KEY,
                             private_key=settings.RECAPTCHA_PRIVATE_KEY)

    content = forms.CharField(
        widget=TinyMCEWidget(
            attrs={'required': False, 'cols': 30, 'rows': 15},
            mce_attrs=({'menubar': False,
                        'plugins': ['advlist autolink lists link image imagetools charmap print preview anchor',
                                    'textcolor searchreplace code insertdatetime media',
                                    'table contextmenu paste code help wordcount autoresize'],
                        'autoresize_min_height': 250,
                        'autoresize_on_init': False,
                        'toolbar': '''
                                insert | undo redo |  formatselect | bold italic backcolor  | 
                                alignjustify | bullist numlist outdent indent | 
                                removeformat | help',
                                ''',
                        'toolbar2': '''''',
                        'content_css': ['//fonts.googleapis.com/css?family=Lato:300,300i,400,400i',
                                        'https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css'],
                        'content_css_cors': 'true',
                        'branding': False,
                        'content_style': 'img {max-width: 100%; height:auto;}',
                        'imagetools_toolbar': "rotateleft rotateright | flipv fliph | editimage imageoptions",
                        })
        )
    )

    class Meta:
        model = Murr
        fields = ('title',  'description', 'content', 'tags', 'categories', 'cover', 'captcha'
                  # 'is_draft', 'is_public'
                  )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(Column('title', css_class='form-group col-12 mb-0')),
            Row(Column('description', css_class='form-group col-12 mb-0')),
            'content',
            Row(
                Column('tags', css_class='form-group col-12 mb-0'),
                Column('categories', css_class='form-group col-12 mb-0'),
                css_class='form-row'
            ),
            Row(
                HTML('''
                <div class='container-fluid form-group formColumn'>
                    <input type="image" 
                        src="{{ form.instance.cover_url | default_if_none:"/static/img/NoImageAvailable.png" }}" 
                        data-toggle="tooltip" data-placement="top" title="Установить обложку для мурра" width="100px" 
                        height="100px" class="rounded bg-light" style="outline: none;" id="cover-img"/>
                </div> 
                '''),
                Column('cover', css_class='inputfile inputfile-3 d-none'),
            ),
        )

        if settings.USE_CAPCHA:
            self.helper.layout.fields.append(Row(Column('captcha', css_class='mx-auto')))

        self.helper.layout.fields.append(Submit('submit', 'Сохранить', css_class='mt-3'))

    def clean_tags(self):
        """Cleaning tags from backslashes and strip html-tags"""

        tags = self.cleaned_data.get('tags')

        tags = [bleach.clean(tag, tags=[], strip=True).replace('/', '') for tag in tags]

        limited = 0
        added = []
        for tag in tags:
            length = len(tag)
            if limited + length > self.LIMIT_LEN_TAGS:
                break

            added.append(tag)
            limited += length
        tags = added

        return filter(bool, tags)


class CommentForm(forms.ModelForm):
    _attrs = {'class': 'form-control', 'placeholder': 'введите ваш комментарий', 'rows': '2'}

    content = forms.CharField(widget=forms.Textarea(attrs=_attrs), label='')
    captcha = ReCaptchaField(
                             public_key=settings.RECAPTCHA_PUBLIC_KEY,
                             private_key=settings.RECAPTCHA_PRIVATE_KEY)

    class Meta:
        model = Comment
        fields = ('content', )
        if settings.USE_CAPCHA:
            fields = ('content', 'captcha')

    def clean_content(self):
        content = self.cleaned_data.get('content')
        content = bleach.clean(content, tags=[], strip=True).strip()
        return content
