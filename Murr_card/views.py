from taggit.models import Tag

from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q, Count
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .forms import CommentForm, MurrForm
from .models import Murr, MurrVisiting, Comment, Category

User = get_user_model()


def murr_list(request, **kwargs):
    """ в kwargs передавать tag_name - для отбора по тегам;
    search_result - отбора по результатам поиска"""

    all_murrs = Murr.objects.filter(is_public=True, is_draft=False)
    if request.user.is_authenticated:
        # all murrs + my drafts
        all_murrs = Murr.objects.filter(Q(is_draft=True, author_id=request.user.id) | Q(is_draft=False))

    tag_name = kwargs.get('tag_name')
    if tag_name:
        tag = get_object_or_404(Tag, name=tag_name)
        all_murrs = all_murrs.filter(tags__name=tag)

    if kwargs.get('search_result'):
        all_murrs = kwargs.get('search_result')

    all_murrs = all_murrs.annotate(comments_total=Count('comments__pk')).order_by('-timestamp')
    paginator = Paginator(all_murrs, 5)
    try:
        page = paginator.page(request.GET.get('page'))
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    context = {'murrs': page, 'last_two': all_murrs[:2], 'categories': Category.objects.all()}
    return render(request, 'Murr_card/murr_list.html', context)


def murr_detail(request, slug):
    murr = get_object_or_404(Murr, slug=slug)
    form = CommentForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.instance.user = request.user
        form.instance.murr = murr
        form.save()
        return HttpResponseRedirect(request.path)
    if request.user.is_authenticated and request.user.pk != murr.author_id:
        MurrVisiting.objects.get_or_create(user=request.user, murr=murr)

    return render(request, 'Murr_card/murr_detail.html', {'murr': murr, 'form': form})


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

    return murr_list(request, **context)


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
    return redirect(reverse('murr_list'))


def comment_cut(request, id):
    comment = get_object_or_404(Comment, pk=id)
    # comment.delete()
    print(f'\n\n{comment} --------------- were here\n\n')
    return redirect(reverse('murr_list'))
