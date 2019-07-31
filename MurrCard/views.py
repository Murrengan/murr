from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Count
from django.http import JsonResponse, HttpResponseForbidden, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string
from django.urls import reverse
from django.views.decorators.http import require_POST
from django.db.models.query import EmptyQuerySet

from .forms import CommentForm, MurrForm
from .likes import LikeProcessor
from .actions import ActionProcessor
from .models import Murr, Comment, MurrAction
from murr.shortcuts import MurrenganPaginator


User = get_user_model()


def murr_list(request):
    """
    http://127.0.0.1:8000/murrs?author=test@test.ru&tag_name=er&tag_name=qwe&category=programming&my&liked
    """
    murrs = Murr.objects.all().annotate(report_count=Count('actions__kind',
                                                           filter=Q(actions__kind=MurrAction.REPORT)
                                                           )).exclude(report_count__gte=5)

    all_searched_murrs = Murr.objects.none()

    if not request.user.is_anonymous:
        actions = [MurrAction.REPORT, MurrAction.HIDE]
        murrs = murrs.exclude(actions__murren=request.user, actions__kind__in=actions)

    query = request.GET.get('q')
    if query:
        query_in_title = Q(title__icontains=query)
        query_in_desc = Q(description__icontains=query)
        query_in_tag = Q(tags__name__icontains=query)
        murrs_by_quick_search = murrs.filter(query_in_title | query_in_tag | query_in_desc)
        all_searched_murrs.union(murrs_by_quick_search)

        if murrs.exists() is False:
            messages.add_message(request, messages.INFO, 'Поиск принес только опыт и 0 информации')

    tag_names = request.GET.get('tag_name')
    if tag_names:
        murrs_by_tag_names = murrs.filter(tags__name__icontains=tag_names)
        all_searched_murrs.union(murrs_by_tag_names)

    categories = request.GET.get('category')
    if categories:
        murrs_by_categories = murrs.filter(categories__icontains=categories)
        all_searched_murrs.union(murrs_by_categories)

    authors = request.GET.get('author')
    if authors:
        murrs_by_authors = murrs.filter(author__username__icontains=authors)
        all_searched_murrs.union(murrs_by_authors)

    if 'my' in request.GET:
        all_searched_murrs = murrs.filter(author=request.user)

    if 'liked' in request.GET:
        murrens_likes = request.user.get_liked_murrs()
        all_searched_murrs = murrs.filter(liked__murr_id__in=murrens_likes)

    if isinstance(all_searched_murrs, EmptyQuerySet):
        murrs = murrs.annotate(comments_total=Count('comments__pk'))
    else:
        murrs = all_searched_murrs.annotate(comments_total=Count('comments__pk'))

    murrs = murrs.order_by('-timestamp')
    page = request.GET.get('page', 1)
    paginator = MurrenganPaginator(murrs.distinct(), 10)
    page = paginator.page(page)
    context = {
        'page': page,
    }
    return render(request, 'MurrCard/murr_list.html', context)


def murr_detail(request, slug):
    """ Show single murr """
    murr = get_object_or_404(Murr, slug=slug)
    form = CommentForm()
    context = {'murr': murr, 'comment_form': form}

    try:
        # TODO when unauthorized user opens murr_detail page, take AttributeError
        murren = murr.author
        client = request.user
        following = client.masters.filter(master_id=murren.pk)
        already_follow = following.exists()
        context.update({
            'murren': murren,
            'already_follow': already_follow})
    except AttributeError:
        pass

    if request.method == 'POST':
        html = render_to_string('MurrCard/includes/_murr-detail_drawer_view.html', context, request)
        return JsonResponse({'html': html})
    context.update({'show_follow': True})
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
    # if not form.is_valid():
    #     return None

    murr_slug = request.POST.get('murr_slug')
    murr = get_object_or_404(Murr, slug=murr_slug)
    form.instance.user = request.user
    form.instance.murr = murr
    form.save()
    template = 'MurrCard/includes/_murr-detail_drawer_comments.html'
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


def save_comment(request, pk, slug, template):
    data = dict()
    # murr = get_object_or_404(Murr, slug=slug)
    # comment = get_object_or_404(murr.get_comments, pk=pk)
    comment = get_object_or_404(Comment, pk=pk)
    if request.is_ajax():
        if request.method == 'POST':
            form = CommentForm(request.POST, instance=comment)
            if form.is_valid():
                form.save()
                data['success'] = True
                data['message'] = 'form inplace saved'
                data['content'] = render_to_string(template, context={'comment': comment}, request=request)
            else:
                data['success'] = False
                data['message'] = 'form is not valid'
            # print(f"{form.cleaned_data['content']}\n\t ==== were saved ====\ncontext:\n\t{context}\n")
        elif request.method == 'GET':
            print(request.GET)
            form = CommentForm(instance=comment)
            data['message'] = 'form inplace send'
            data['success'] = True
            data['html_form'] = render_to_string(template, context={'form': form}, request=request)
    else:
        raise Http404

    return JsonResponse(data)


@require_POST
@login_required
def comment_edit(request):
    author = request.user
    pk = request.POST.get('pk')
    comment = get_object_or_404(Comment, pk=pk, user=author)
    form = CommentForm(request.POST, instance=comment, auto_id='comment-edit-%s')
    if form.is_valid():
        context = {'edit_form': form}
        html = render_to_string('MurrCard/includes/_comment_edit_form.html', context, request)
        return JsonResponse({'html': html})
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
        template = 'MurrCard/includes/_murr-detail_drawer_comments.html'
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


@require_POST
@login_required
def murr_action(request):
    raw_data = request.POST.dict()
    processor = ActionProcessor(raw_data)
    processor.process()
    if processor.errors:
        return JsonResponse({'error': processor.errors})
    processor.save()
    return JsonResponse({'ok': True})
