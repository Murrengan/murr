from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

User = get_user_model()

# from .forms import MurrenRegisterForm


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
#     return render(request, 'registration/singup.html', {
#         'form': form
#     })


@login_required
def profile(request):
    return render(request, 'Murren/profile.html')
