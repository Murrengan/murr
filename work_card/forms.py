from django.forms import ModelForm

from work_card.models import WorkCard


class WorkCardForm(ModelForm):
    class Meta:
        model = WorkCard
        fields = ('title', 'description', 'contact', 'city', 'rubric')
