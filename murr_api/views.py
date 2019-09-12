from django.http import JsonResponse
from rest_framework import generics

from MurrCard.models import Murr
from MurrCard.serializers import MurrSerializer
from Murren.models import Murren
from murr_api.permissions import IsAuthorOrReadOnly
from .serializers import MurrenSerializer


class MurrenList(generics.ListAPIView):
    queryset = Murren.objects.all()
    serializer_class = MurrenSerializer


class MurrenById(generics.RetrieveAPIView):

    queryset = Murren.objects.all()
    serializer_class = MurrenSerializer


class MurrList(generics.ListCreateAPIView):

    queryset = Murr.objects.all()
    serializer_class = MurrSerializer


class MurrDetail(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Murr.objects.all()
    serializer_class = MurrSerializer


def start(request):
    data = {'base_card_img_url': 'http://127.0.0.1:8000/static/img/murr_game/Gorbug.png'}
    return JsonResponse(data, status=200)


def hell_gate(request):
    data = {'base_card_img_url': 'http://127.0.0.1:8000/static/img/murr_game/hell_gate.png'}
    return JsonResponse(data, status=200)
