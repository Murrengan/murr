from taggit.models import Tag

from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q, Count
from django.http import JsonResponse, HttpResponseForbidden, Http404
from django.middleware.csrf import get_token
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string
from django.urls import reverse
from django.views.decorators.http import require_http_methods, require_POST
from taggit.models import Tag

from .forms import CommentForm, MurrForm, CommentEditForm
from .likes import LikeProcessor
from .models import Murr, Comment

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

    category = kwargs.get('category')
    if category:
        murrs = murrs.filter(categories=category)

    murrs = murrs.annotate(comments_total=Count('comments__pk'))
    murrs = murrs.order_by('-timestamp')
    paginator = Paginator(murrs.distinct(), 5)
    page = paginator.get_page(request.GET.get('page'))

    context = {
        'page': page,
        'csrf': get_token(request),
    }
    return render(request, 'MurrCard/murr_list.html', context)


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
        'csrf': get_token(request),
    }
    return render(request, 'MurrCard/murr_list.html', context)


def murr_detail(request, slug):
    """ Show single murr with its comments """
    murr = get_object_or_404(Murr, slug=slug)
    if request.method == 'POST':
        context = {'murr': murr}
        html = render_to_string('MurrCard/includes/_murr_detail_content.html', context, request)
        return JsonResponse({'html': html})

    form = CommentForm()
    context = {'murr': murr, 'comment_form': form, 'csrf': get_token(request)}
    return render(request, 'MurrCard/murr_detail.html', context)


@login_required
def murr_create(request):
    title = 'Создай'
    form = MurrForm(request.POST or None, request.FILES or None)
    author = request.user
    if request.method == 'POST' and form.is_valid():
        form.instance.author = author
        form.save()
        return redirect(reverse('murr_detail', kwargs={
            'slug': form.instance.slug
        }))

    context = {'title': title, 'form': form}
    return render(request, 'MurrCard/murr_create.html', context)


def murr_update(request, slug):
    template = 'MurrCard/murr_create.html'
    title = 'Измени'
    author = request.user
    murr = get_object_or_404(Murr, slug=slug, author=author)
    form = MurrForm(
        request.POST or None,
        request.FILES or None,
        instance=murr)
    if request.method == 'POST' and form.is_valid():
        form.instance.author = author
        form.save()
        return redirect(reverse('murr_detail', kwargs={
            'slug': form.instance.slug
        }))

    context = {'title': title, 'form': form}
    return render(request, template, context)


@login_required(login_url='/accounts/login')
def murr_delete(request, slug):
    if request.user.is_authenticated:
        user = request.user
        murr = get_object_or_404(Murr, slug=slug, author=user)
        murr.delete()
        return redirect(reverse('murr_list'))
    else:
        return HttpResponseForbidden()


@require_POST
@login_required
def comment_add(request):
    form = CommentForm(request.POST)
    if not form.is_valid():
        return None

    murr_slug = request.POST.get('murr_slug')
    murr = get_object_or_404(Murr, slug=murr_slug)
    form.instance.user = request.user
    form.instance.murr = murr
    form.save()
    template = 'MurrCard/includes/_murr_detail_comments.html'
    comments = render_to_string(template, {'murr': murr}, request)
    return JsonResponse({'comments': comments})


@require_POST
@login_required
def comment_delete(request):
    author = request.user
    pk = request.POST.get('pk')
    comment = get_object_or_404(Comment, pk=pk, user=author)
    comment.delete()
    return JsonResponse({'ok': True})


@require_POST
@login_required
def comment_update(request):
    author = request.user
    pk = request.POST.get('pk')
    comment = get_object_or_404(Comment, pk=pk, user=author)
    form = CommentForm(request.POST, instance=comment)
    if form.is_valid():
        form.save()
        murr_slug = request.POST.get('murr_slug')
        murr = get_object_or_404(Murr, slug=murr_slug)
        template = 'MurrCard/includes/_murr_detail_comments.html'
        comments = render_to_string(template, {'murr': murr}, request)
        return JsonResponse({'comments': comments})


@login_required()
def like(request):
    if request.method == 'GET':
        raise Http404

    raw_data = request.POST.dict()
    processor = LikeProcessor(raw_data)
    processor.process()
    if processor.errors:
        return JsonResponse({'error': processor.errors})

    processor.save()
    murr = request.POST.get('murr')
    likes = Murr.objects.get(slug=murr).liked.count() or ''
    return JsonResponse({'ok': True, 'likes': likes})


@login_required()
def unlike(request):
    if request.method == 'GET':
        raise Http404

    raw_data = request.POST.dict()
    processor = LikeProcessor(raw_data)
    processor.process()
    if processor.errors:
        return JsonResponse({'error': processor.errors})

    processor.delete()
    murr = request.POST.get('murr')
    likes = Murr.objects.get(slug=murr).liked.count() or ''
    return JsonResponse({'ok': True, 'likes': likes})
