from django.shortcuts import render

from Murr_card.models import Murr


def murrs_list(requset):
    murrs = Murr.objects.all()
    context = {
        'murrs': murrs
    }
    return render(requset, 'Murr_card/murr_list.html', context)


def murr_detail(request, slag):

    murr = Murr.objects.get(slag__iexact=slag)

    context = {
        'murr': murr
    }

    return render(request, 'Murr_card/murr_detail.html', context)
