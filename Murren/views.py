from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import ProfileMurrenForm

User = get_user_model()


def landing(request):
    return render(request, 'Murr_card/landing.html')


def count_murren(request):
    count = User.objects.count()
    return render(request, 'Murren/count_murren.html', {
        'count': count
    })


def signup(request):
    pass
#     if request.method == 'POST':
#         form = MurrenRegisterForm(request.POST)
#
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             form.save()
#             messages.success(request, f'Account created for {username}!')
#             return redirect('login')
#     else:
#         form = MurrenRegisterForm()
#     return render(request, 'registration/signup.html', {
#         'form': form
#     })


@login_required
def profile(request):
    if request.method == 'POST':
        # instance = request.user показывает, что работа происходит именно для текущего клиента
        murren_form = ProfileMurrenForm(request.POST, request.FILES, instance=request.user)
        if murren_form.is_valid():
            murren_form.save()
            # TODO Добавить отображение messages from django
            messages.success(request, f'Твой профайл успешно изменен')
            return redirect('profile')
    else:
        murren_form = ProfileMurrenForm(instance=request.user)

    context = {
        'murren_form': murren_form,
    }

    return render(request, 'Murren/profile.html', context)
