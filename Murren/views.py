from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, reverse, redirect

from .forms import ProfileMurrenForm

User = get_user_model()


def landing(request):
    return render(request, 'Murr_card/landing.html')


def redirect_view(request):
    if request.user.is_authenticated:
        return redirect(reverse('murr_list'))
    else:
        return redirect(reverse('account_login'))


def murren_profile(request, username):
    murren_data = User.objects.get(username=username)
    return render(request, 'Murren/murren_profile.html', {
        'murren_data': murren_data
    })


@login_required
def profile(request):
    if request.method == 'POST':
        # instance = request.user shows that the work is done for the exactly current client
        murren_form = ProfileMurrenForm(request.POST, request.FILES, instance=request.user)
        if murren_form.is_valid():
            murren_form.save()
            messages.success(request, f'Твой профайл успешно изменен')
            return redirect('profile')
    else:
        murren_form = ProfileMurrenForm(instance=request.user)

    context = {
        'murren_form': murren_form,
    }

    return render(request, 'Murren/profile.html', context)
