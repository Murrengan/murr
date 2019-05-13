from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import JsonResponse, Http404
from django.middleware.csrf import get_token
from django.shortcuts import render, redirect

from MurrCard.models import Murr
from .following import FollowingProcessor
from .forms import ProfileMurrenForm

User = get_user_model()


def profile(request, username):
    murren = User.objects.get(username=username)
    client = request.user.pk and request.user
    following = client and client.masters.filter(master_id=murren.pk)
    already_follow = client and following.exists()
    context = {
        'murren': murren,
        'csrf': get_token(request),
        'already_follow': already_follow
    }
    return render(request, 'Murren/murren_profile.html', context)


def follow(request):
    if request.method == 'GET':
        raise Http404

    raw_data = request.POST.dict()
    raw_data['follower'] = request.user.pk
    processor = FollowingProcessor(raw_data)
    processor.process()
    if processor.errors:
        return JsonResponse({'error': 'follow not allowed'})

    processor.save()
    return JsonResponse({'ok': True})


def unfollow(request):
    if request.method == 'GET':
        raise Http404

    raw_data = request.POST.dict()
    raw_data['follower'] = request.user.pk
    processor = FollowingProcessor(raw_data)
    processor.process()
    if processor.errors:
        return JsonResponse({'error': 'follow not allowed'})

    processor.delete()
    return JsonResponse({'ok': True})


@login_required
def murren_edit(request):
    if request.method == 'POST':
        form = ProfileMurrenForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Твой профайл успешно изменен')
            return redirect('edit')

    else:
        form = ProfileMurrenForm(instance=request.user)

    context = {'murren_form': form}

    return render(request, 'Murren/murren_edit.html', context)


def landing(request):
    return render(request, 'MurrCard/landing.html')


def show_all_liked_murrs(request):
    murrens_likes = request.user.get_liked_murrs()
    liked_murrs = Murr.objects.filter(liked__murr_id__in=murrens_likes)
    murrs = liked_murrs.order_by('timestamp')
    paginator = Paginator(murrs.distinct(), 5)
    page = paginator.get_page(request.GET.get('page'))

    context = {
        'page': page,
    }
    return render(request, 'MurrCard/murr_list.html', context)
