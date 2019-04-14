from django.shortcuts import render

from mg_engine.models import Blockman


def mg_engine(request):
    data = Blockman.objects.get_or_create(author=request.user)[0]
    return render(request, 'mg_engine/mg_engine_start.html', {'data': data})
