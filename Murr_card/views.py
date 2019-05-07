from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q, Count
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from taggit.models import Tag

from .forms import CommentForm, MurrForm, CommentEditForm
from .models import Murr, Comment, Category

User = get_user_model()


def murr_list(request, **kwargs):
    """
    Output all murrs or murrs that filtered by tag
    or murrs queryset from kwargs
    """
    murrs = Murr.objects.all()
    tag_name = kwargs.get('tag_name')
    if tag_name:
        tag = get_object_or_404(Tag, name=tag_name)
        murrs = murrs.filter(tags__name=tag)

    murrs = murrs.annotate(comments_total=Count('comments__pk'))
    murrs = murrs.order_by('-timestamp')
    paginator = Paginator(murrs.distinct(), 5)
    page = paginator.get_page(request.GET.get('page'))

    context = {
        'page': page,
        'categories': Category.objects.all(),
    }
    return render(request, 'Murr_card/murr_list.html', context)


def search(request):
    """ Filter murrs by search query and pass queryser to murr_list view """
    murrs = Murr.objects.all()
    query = request.GET.get('q')
    if query:
        query_in_title = Q(title__icontains=query)
        query_in_desc = Q(description__icontains=query)
        murrs = murrs.filter(query_in_title | query_in_desc)
        if murrs.exists() is False:
            messages.add_message(request, messages.INFO, 'Поиск принес только опыт и 0 информации')

    murrs = murrs.annotate(comments_total=Count('comments__pk'))
    murrs = murrs.order_by('-timestamp')
    paginator = Paginator(murrs.distinct(), 5)
    page = paginator.get_page(request.GET.get('page'))

    context = {
        'page': page,
        'search_query': f'q={query}&',
        'categories': Category.objects.all(),
    }
    return render(request, 'Murr_card/murr_list.html', context)


def murr_detail(request, slug):
    murr = get_object_or_404(Murr, slug=slug)
    form = CommentForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.instance.user = request.user
        form.instance.murr = murr
        form.save()
        return HttpResponseRedirect(request.path)

    context = {'murr': murr, 'form': form}
    return render(request, 'Murr_card/murr_detail.html', context)


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

    context = {'title': title, 'form': form}
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

    context = {'title': title, 'form': form}
    return render(request, template, context)


def murr_delete(request, slug):
    murr = get_object_or_404(Murr, slug=slug)
    murr.delete()
    return redirect(reverse('murr_list'))


def comment_cut(request, id):
    comment = get_object_or_404(Comment, pk=id)
    comment.delete()
    return JsonResponse({'success': True})


@login_required
def comment_edit(request, id):
    data = dict()
    # template = 'Murr_card/comment_edit.ajax.html'
    comment = get_object_or_404(Comment, pk=id)
    form = CommentEditForm(request.POST or None, instance=comment)
    if request.method == 'POST' and form.is_valid():
        # print(f"{form.cleaned_data['content'],form.cleaned_data['reply']}\n\t ==== were saved ====\n")
        print(f"{form.cleaned_data['content']}\n\t ==== were saved ====\n")
        return redirect(reverse('murr_list'))

    context = {'title': '-EDIT-', 'form': form, 'comment':comment.content,}
    # render_to_string
    # return JsonResponse({'success': True})
    return render(request, 'Murr_card/comment_edit.ajax.html', context)


def comment_reply(request, id):
    # comment = get_object_or_404(Comment, pk=id)
    # render_to_string
    # return JsonResponse({'success': True})
    pass
