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
    text = """""<br>
                    <span class="hell-font">"Оставьте всякую надежду, вы, входящие"</span><br><br>

                    Горбаг - город на границе у врат ада.<br><br>

                    Первая территория, куда попадают души.<br>
                    Путники наполняют таверны золотом.<br>
                    Теплый кров спасает от ужаса ночи.<br>
                    Надежда еще жива...<br><br>

                    Я стою перед открытой дверью в красную таверну.<br><br>
                    Запах вкусной курочки доносится из шумного здания.<br>
                    """""
    show_btn = [
        {
            'btb': 'show_hell_gate__btn',
            'btn_text': 'Взглянуть на ворота',
            'btn_color': '#14c8ff',
            'def_on_click': 'look_at_hell_gate',

        },

        {
            'btb': 'show_tawern_card__btn',
            'btn_text': 'Войти в таверну',
            'btn_color': '#ff91fb',
            'def_on_click': 'come_to_tawern',
        }

    ]

    data = {'base_card_img_url': '', 'base_card_text': text, 'show_btn': show_btn}
    return JsonResponse(data, status=200)


def hell_gate(request):
    text = """""<br>
        Врата ада<br>
        и жарко и холодно.<br>
        Я представлял их по другому.<br><br>
        
        Их образ всегда перед моими глазами.<br>
        Душа наполняется трепетом и горем.<br>
        характеристики -5<br><br>


        <span class="hell-font">"Lasciate ogni speranza, voi ch’entrate"</span><br>

        """""
    show_btn = ['show_come_to_tawern__btn']

    data = {'base_card_img_url': 'http://127.0.0.1:8000/static/img/murr_game/hell_gate.png',
            'base_card_text': text,
            'show_btn': show_btn}
    return JsonResponse(data, status=200)
