from django.contrib.auth.decorators import login_required
from django.shortcuts import reverse, redirect, render


@login_required
def redirect_view(request):
    return redirect(reverse('murr_list'))


def about(request):
    return render(request, 'about.html')
