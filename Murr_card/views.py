from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count, Q
from django.shortcuts import render, get_object_or_404

from .forms import CommentForm
from .models import Murr


def murrs_list(requset):
    all_categories_count = get_all_categories_count()[0:5]
    all_murrs = Murr.objects.filter().order_by('-timestamp')
    paginator = Paginator(all_murrs, 4)
    page_request_ver = 'page'
    page = requset.GET.get(page_request_ver)
    try:
        paginator_queriset = paginator.page(page)
    except PageNotAnInteger:
        paginator_queriset = paginator.page(1)
    except EmptyPage:
        paginator_queriset = paginator.page(paginator.num_pages)

    latest = Murr.objects.order_by('-timestamp')[0:2]
    context = {
        'murrs': paginator_queriset,
        'page_request_ver': page_request_ver,

        'all_categories_count': all_categories_count,
        'latest': latest
    }
    return render(requset, 'Murr_card/murr_list.html', context)


def murr_detail(request, pk):
    murr_detail = get_object_or_404(Murr, pk=pk)
    form = CommentForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.user = request.user
            # TODO что это?
            form.instance.post = murr_detail
            form.save()
    context = {
        'murr_detail': murr_detail,
        'form': form
    }
    return render(request, 'Murr_card/murr_detail.html', context)


def get_all_categories_count():
    # Получаем Имя значения values('categories__title') и их колличество (categories__title отправляем к модели)
    all_categories_count = Murr.objects.values('categories__title').annotate(Count('categories__title'))
    return all_categories_count


def search(request):
    all_murrs = Murr.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = all_murrs.filter(
            Q(title__contains=query) |
            Q(description__contains=query)
        ).distinct()

    context = {
        'search_result': queryset
    }
    return render(request, 'Murr_card/search_result.html', context)
