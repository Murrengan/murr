from django.shortcuts import render

from MurrCard.models import Murr


def dashboard(request):

    murrs = Murr.objects.filter(author__followers__follower__pk=request.user.pk)

    context = {
        'murrs': murrs
    }

    return render(request, 'Dashboard/dashboard.html', context)
