from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from Murren.models import MurrenProfile


def landing(request):
    return render(request, 'Murr_card/landing.html')


def count_murren(request):
    count = MurrenProfile.objects.count()
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
    data = MurrenProfile.objects.get_or_create(user=request.user)[0]
    return render(request, 'Murren/profile.html', {'data': data})
