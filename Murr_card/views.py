from django.shortcuts import render

from Murr_card.models import Murr


def murrs_list(requset):
    queriset = Murr.objects.filter(featured=True).order_by('-timestamp')
    latest = Murr.objects.order_by('-timestamp')[0:2]
    context = {
        'murrs': queriset,
        'latest': latest
    }
    return render(requset, 'Murr_card/murr_list.html', context)
