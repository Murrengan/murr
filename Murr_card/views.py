from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count, Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .forms import CommentForm, MurrForm
from .models import Murr, MurrView
from django.contrib.auth import get_user_model


User = get_user_model()


def murrs_list(request):
    all_categories_count = get_all_categories_count()[0:5]
    all_murrs = Murr.objects.filter(is_draft=False).filter(is_public=True).order_by('-timestamp')
    if request.user.is_authenticated:
        # my_drafts = False if # моказать усі пости усіх + МОЇ чорновики
        all_murrs = Murr.objects.filter(is_draft=False).order_by('-timestamp')
    paginator = Paginator(all_murrs, 4)
    page_request_ver = 'page'
    page = request.GET.get(page_request_ver)
    try:
        paginator_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginator_queryset = paginator.page(1)
    except EmptyPage:
        paginator_queryset = paginator.page(paginator.num_pages)

    # latest = Murr.objects.order_by('-timestamp')[0:2]
    latest = all_murrs[0:2]
    context = {
        'murrs': paginator_queryset,
        'page_request_ver': page_request_ver,
        'all_categories_count': all_categories_count,
        'latest': latest
    }
    return render(request, 'Murr_card/murr_list.html', context)


def murr_detail(request, pk):
    murr_detail = get_object_or_404(Murr, pk=pk)
    form = CommentForm(request.POST or None)

    # себя не добавляем в просмотры
    if request.user.is_authenticated and request.user.id != murr_detail.author_id:
        MurrView.objects.get_or_create(user=request.user, murr=murr_detail)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.user = request.user
            form.instance.murr = murr_detail
            form.save()
            return HttpResponseRedirect(request.path)
    context = {
        'murr_detail': murr_detail,
        'form': form
    }
    return render(request, 'Murr_card/murr_detail.html', context)


def murr_is_hit(request):
    print(f"\t\tIP = {request.META.get('REMOTE_ADDR')}\n\n")
    return


def get_all_categories_count():
    # Получаем Имя значения values('categories__title') и их колличество (categories__title отправляем к модели)
    all_categories_count = Murr.objects.values('categories__title').annotate(Count('categories__title'))
    return all_categories_count


def search(request):
    queryset = ''
    template = 'Murr_card/search_result.html'
    all_murrs = Murr.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = all_murrs.filter(
            # в постгре будет работать через query.lower()?
            Q(title__icontains=query) |
            Q(description__icontains=query)
        ).distinct()

    context = {
        'search_result': queryset
    }
    return render(request, template, context)


def murr_create(request):
    template = 'Murr_card/murr_create.html'
    title = 'Create'
    form = MurrForm(request.POST or None, request.FILES or None)
    author = request.user
    if request.method == 'POST':
        if form.is_valid():
            form.instance.author = author
            form.save()
            return redirect(reverse('murr_detail', kwargs={
                'pk': form.instance.pk
            }))
    context = {
        'title': title,
        'form': form
    }
    return render(request, template, context)


def murr_update(request, pk):
    template = 'Murr_card/murr_create.html'
    title = 'Update'
    murr = get_object_or_404(Murr, id=pk)
    form = MurrForm(
        request.POST or None,
        request.FILES or None,
        instance=murr)
    author = request.user
    if request.method == 'POST':
        if form.is_valid():
            form.instance.author = author
            form.save()
            return redirect(reverse('murr_detail', kwargs={
                'pk': form.instance.pk
            }))
    context = {
        'title': title,
        'form': form
    }
    return render(request, template, context)


def murr_delete(request, pk):
    murr = get_object_or_404(Murr, id=pk)
    murr.delete()
    return redirect(reverse('murrs_list'))
