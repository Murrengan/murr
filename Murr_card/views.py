from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count, Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from taggit.models import Tag

from .forms import CommentForm, MurrForm
from .models import Murr, MurrVisiting, Comment

User = get_user_model()


def murrs_list(request, tag_name=None):
    all_categories_count = get_all_categories_count()[0:5]
    all_murrs = Murr.objects.filter(is_draft=False).filter(is_public=True).order_by('-timestamp')
    if request.user.is_authenticated:
        # ----- показать все посты (мурры) всех ПЛЮС МОИ черновики ----
        all_murrs = Murr.objects.filter(Q(is_draft=True) & Q(author_id=request.user.id) |
                                        Q(is_draft=False)).order_by('-timestamp')
    if tag_name:
        tag = get_object_or_404(Tag, name=tag_name)
        all_murrs = all_murrs.filter(tags__in=[tag])

    paginator = Paginator(all_murrs, 5)
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


def murr_detail(request, slug):
    murr_detail = get_object_or_404(Murr, slug=slug)
    form = CommentForm(request.POST or None)

    # себя не добавляем в просмотры
    if request.user.is_authenticated and request.user.id != murr_detail.author_id:
        MurrVisiting.objects.get_or_create(user=request.user, murr=murr_detail)
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
    # print(f"\t\tIP = {request.META.get('REMOTE_ADDR')}\n\n")
    return

          
def get_all_categories_count():
    # Получаем Имя значения values('categories__title') и их колличество (categories__title отправляем к модели)
    all_categories_count = Murr.objects.values('categories__title').annotate(Count('categories__title'))
    return all_categories_count


def search(request):
    queryset = ''
    all_murrs = Murr.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = all_murrs.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        ).distinct()

    context = {
        'search_result': queryset
    }
    return render(request, 'Murr_card/search_result.html', context)


@login_required
def murr_create(request):
    title = 'Создай'
    form = MurrForm(request.POST or None, request.FILES or None)
    author = request.user
    if request.method == 'POST':
        if form.is_valid():
            form.instance.author = author
            form.save()
            return redirect(reverse('murr_detail', kwargs={
                'slug': form.instance.slug
            }))
    context = {
        'title': title,
        'form': form
    }
    return render(request, 'Murr_card/murr_create.html', context)


def murr_update(request, slug):
    template = 'Murr_card/murr_create.html'
    title = 'Измени'
    murr = get_object_or_404(Murr, slug=slug)
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
                'slug': form.instance.slug
            }))
    context = {
        'title': title,
        'form': form
    }
    return render(request, template, context)


def murr_delete(request, slug):
    murr = get_object_or_404(Murr, slug=slug)
    murr.delete()
    return redirect(reverse('murrs_list'))


def comment_cut(request, id):
    comment = get_object_or_404(Comment, pk=id)
    # comment.delete()
    print(f'\n\n{comment} --------------- were here\n\n')
    return redirect(reverse('murrs_list'))
