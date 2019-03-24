from django.shortcuts import render

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
