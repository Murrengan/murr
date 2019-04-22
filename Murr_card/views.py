from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q, Count
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from taggit.models import Tag

from .forms import CommentForm, MurrForm
from .models import Murr, MurrVisiting, Comment, Category

User = get_user_model()


def murr_list(request, **kwargs):
    """ Output all murrs or murrs that filtered by tag
        or murrs queryset from kwargs"""

    murrs = Murr.objects.filter(is_public=True, is_draft=False)

    if request.user.is_authenticated:
        # all murrs + my drafts
        availabled = Q(is_draft=True, author_id=request.user.id) | Q(is_draft=False)
        murrs = Murr.objects.filter(availabled)

    tag_name = kwargs.get('tag_name')
    if tag_name:
        tag = get_object_or_404(Tag, name=tag_name)
        murrs = murrs.filter(tags__name=tag)

    found_murrs = kwargs.get('search_result')
    search_query = kwargs.get('search_query', '')
    if found_murrs is not None:
        murrs = found_murrs
        search_query = f'q={search_query}&'

    murrs = murrs.annotate(comments_total=Count('comments__pk')).order_by('-timestamp')
    paginator = Paginator(murrs, 5)
    try:
        page = paginator.page(request.GET.get('page'))
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    context = {
        'page': page,
        'search_query': search_query,
        'categories': Category.objects.all(),
    }



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

    context = {'murr': murr, 'form': form}
    return render(request, 'Murr_card/murr_detail.html', context)


def search(request):
    """Filter murrs by search query and pass queryser to murr_list view"""

    murrs = Murr.objects.none()
    query = request.GET.get('q')
    if query:
        search_fields = Q(title__icontains=query) | Q(description__icontains=query)
        murrs = Murr.objects.filter(search_fields).distinct()

    return murr_list(request, search_result=murrs, search_query=query)



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
    ''' удалить мурр '''
    murr = get_object_or_404(Murr, slug=slug)
    murr.delete()
    return redirect(reverse('murr_list'))


def comment_cut(request, id):
    comment = get_object_or_404(Comment, pk=id)
    # comment.delete()
    print(f'\n\n{comment} --------------- were here\n\n')
    return redirect(reverse('murr_list'))


def comment_cut(request, id):
    ''' удалить комментарий '''
    comment = get_object_or_404(Comment, pk=id)
    comment.delete()
    return JsonResponse({'success': True})


def comment_edit(request, id):
    ''' изменить комментарий'''
    data = dict()
    comment = get_object_or_404(Comment, pk=id)
    # comment.delete()
    # render_to_string
    return JsonResponse({'success': True})


def comment_reply(request, id):
    ''' ответ на комментарий'''
    comment = get_object_or_404(Comment, pk=id)
    # comment.delete()
    return JsonResponse({'success': True})
