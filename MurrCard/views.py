from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q, Count
from django.http import HttpResponseRedirect, JsonResponse, HttpResponseForbidden, Http404
from django.middleware.csrf import get_token
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from taggit.models import Tag

from .forms import CommentForm, MurrForm, CommentEditForm
from .likes import LikeProcessor
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
        'csrf': get_token(request),
        'categories': Category.objects.all(),
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
        'categories': Category.objects.all(),
    }
    return render(request, 'MurrCard/murr_list.html', context)


def murr_detail(request, slug):
    """ Show single murr with its comments """
    murr = get_object_or_404(Murr, slug=slug)
    form = CommentForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.instance.user = request.user
        form.instance.murr = murr
        form.save()
        if request.is_ajax():
            data = dict()
            data['comments_list'] = render_to_string(
                'MurrCard/includes/_murr_details_comments.html',
                {'murr': murr},
                request=request
            )
            data['success'] = True
            return JsonResponse(data)
        else:
            return HttpResponseRedirect(request.path)

    context = {'murr': murr, 'form': form}
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


@login_required(login_url='/account_login')
def comment_cut(request, slug, pk):
    if request.user.is_authenticated:
        author = request.user
        comment = get_object_or_404(Comment, pk=pk, user=author)
        comment.delete()
        return JsonResponse({'success': True})
    else:
        HttpResponseForbidden()


@login_required
@require_http_methods(["GET", "POST"])
# @require_POST
def comment_edit(request, pk, slug):
    data = dict()
    murr = get_object_or_404(Murr, slug=slug)
    comment = get_object_or_404(murr.get_comments, pk=pk)
    context = {'title': '-EDIT- ' + slug, 'pk':pk, 'slug':slug}
    if request.is_ajax():
        if request.method == 'POST':
            form = CommentEditForm(request.POST, instance=comment)
            if form.is_valid():
                  form.save()
                  data['success'] = True
                  data['message'] = 'form inplace saved'
                  data['content'] = render_to_string(
                      'MurrCard/includes/_ajaxify_comment_body.html',
                      {'comment':comment},
                      request=request
                  )
            else:
                data['success'] = False
                data['message'] = 'form is not valid'
                context['form'] = form
            print(f"{form.cleaned_data['content']}\n\t ==== were saved ====\ncontext:\n\t{context}\n")
        elif request.method == 'GET':
            print(request.GET)
            form = CommentEditForm(instance=comment)
            context['form'] = form
            data['message'] = 'form inplace send'
            data['success'] = True
            data['html_form'] = render_to_string('MurrCard/comment_edit.ajax.html', context, request=request)
            # return JsonResponse({'success': True})
    else:
        raise Http404

    return JsonResponse(data)



def comment_reply(request, pk):
    # data = dict()
    # comment = get_object_or_404(Comment, pk=id)
    # render_to_string
    # return JsonResponse({'success': True})
    return None


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
