from django.shortcuts import reverse, redirect, render


def redirect_view(request):
    if request.user.is_authenticated:
        return redirect(reverse('murr_list'))
    return redirect(reverse('about'))


def about(request):
    return render(request, 'about.html')
