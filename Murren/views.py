from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, Http404
from django.middleware.csrf import get_token
from django.shortcuts import render, reverse, redirect, get_object_or_404

from .forms import ProfileMurrenForm, MurrenFollower
from .models import Follower

User = get_user_model()


def redirect_view(request):
    if request.user.is_authenticated:
        return redirect(reverse('murr_list'))
    return redirect(reverse('account_login'))


def profile(request, username):
    murren = User.objects.get(username=username)
    client = request.user.pk and request.user
    following = client and client.following.filter(following_id=murren.pk)
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

    form_data = request.POST.dict()
    form_data['follower'] = request.user.pk
    form = MurrenFollower(form_data)
    if form.is_valid():
        form.save()
        return JsonResponse({'ok': True})
    return JsonResponse({'error': 'follow not allowed'})


def unfollow(request):
    if request.method == 'GET':
        raise Http404

    following = get_object_or_404(Follower, follower_id=request.user.pk)
    form_data = request.POST.dict()
    form_data['follower'] = request.user.pk
    form = MurrenFollower(form_data, instance=following)
    if form.is_valid():
        following.delete()
        return JsonResponse({'ok': True})
    return JsonResponse({'error': 'unfollow not allowed'})


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
    return render(request, 'Murr_card/landing.html')
