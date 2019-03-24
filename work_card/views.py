from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from work_card.forms import WorkCardForm
from .models import WorkCard, Rubric


def index(request):
    works = WorkCard.objects.all()
    rubrics = Rubric.objects.all()
    context = {'works': works, 'rubrics': rubrics}
    return render(request, 'index.html', context)


def by_rubric(request, rubric_id):
    works_lists_by_rubric = WorkCard.objects.filter(rubric=rubric_id)
    all_rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {
        'works_lists_by_rubric_id': works_lists_by_rubric,
        'all_rubrics': all_rubrics,
        'current_rubric': current_rubric
    }
    return render(request, 'by_rubric.html', context)


class WorkCardCreateView(CreateView):
    template_name = 'work_card/create_work_card.html'
    form_class = WorkCardForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context
