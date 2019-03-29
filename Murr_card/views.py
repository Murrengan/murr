from django.shortcuts import render, get_object_or_404

from .models import Murr


def murrs_list(requset):
    queriset = Murr.objects.filter(featured=True).order_by('-timestamp')
    latest = Murr.objects.order_by('-timestamp')[0:2]
    context = {
        'murrs': queriset,
        'latest': latest
    }
    return render(requset, 'Murr_card/murr_list.html', context)


def murr_detail(requset, pk):
    murr_detail = get_object_or_404(Murr, pk=pk)
    context = {
        'murr_detail': murr_detail
    }
    return render(requset, 'Murr_card/murr_detail.html', context)
