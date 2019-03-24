from django.forms import ModelForm

from work_card.models import WorkCard


class WorkCardForm(ModelForm):
    class Meta:
        model = WorkCard
        fields = ('title', 'description', 'contact', 'city', 'rubric')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
            })