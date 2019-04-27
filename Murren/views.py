from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, reverse, redirect
from django.http import  JsonResponse


from .forms import ProfileMurrenForm

User = get_user_model()


def redirect_view(request):
    if request.user.is_authenticated:
        return redirect(reverse('murr_list'))
    return redirect(reverse('account_login'))


def profile(request, username):
    context = {'murren_data': User.objects.get(username=username)}
    return render(request, 'Murren/murren_profile.html', context)


def follow(request, username):
    return JsonResponse({'ok': True})


@login_required
def murren_edit(request):
    form = ProfileMurrenForm(request.POST, request.FILES, instance=request.user)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Твой профайл успешно изменен')
        return redirect('edit')

    context = {'murren_form': form}
    return render(request, 'Murren/murren_edit.html', context)


def landing(request):
    return render(request, 'Murr_card/landing.html')
