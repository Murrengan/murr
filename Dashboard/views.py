from django.shortcuts import render

from Murren.models import Murren


def dashboard(request):
    murrens = Murren.objects.filter(followers__follower__pk=request.user.pk)
    context = {
        'murrens': murrens
    }
    return render(request, 'Dashboard/dashboard.html', context)
