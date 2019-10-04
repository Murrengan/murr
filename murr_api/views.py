from django.contrib.auth import get_user_model
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


User = get_user_model()


def start(request):
    text = """\"\"\"<br>
        <span class="hell-font">"Оставьте всякую надежду, вы, входящие"</span><br><br>
        
        Горбаг - город у врат ада.<br><br>
        
        Первая территория, куда попадают души.<br>
        Путники наполняют таверны золотом.<br>
        Теплый кров спасает от ужаса ночи.<br>
        Надежда еще жива...<br><br>
        
        Я стою перед открытой дверью в красную таверну.<br><br>
        
        Запах вкусной курочки доносится из шумного здания.<br>
        \"\"\""""

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
    # murren_data = 'Привет мои сладкие мурр =))))'
    #
    # data = {'murren_id': request.user.id, 'base_card_img_url': '', 'base_card_text': text,
    #         'show_btn': show_btn, 'murren_data': murren_data}
    murren = User.objects.get(username=request.user.username)
    data = {'murren_id': murren.id, 'murren_avatar_img': murren.profile_picture.url,
            'base_card_text': text, 'show_btn': show_btn}
    return JsonResponse(data, status=200)


def look_at_hell_gate(request):
    text = """\"\"\"<br>
        Врата ада.<br>
        И жарко и холодно.<br>
        Я представлял их по другому.<br><br>
        
        Их образ всегда перед моими глазами.<br>
        Душа наполняется трепетом и горем.<br>
        характеристики -5<br><br>


        <span class="hell-font">"Lasciate ogni speranza, voi ch’entrate"</span><br>
        \"\"\""""

    show_btn = [
        {
            'btb': 'show_tawern_card__btn',
            'btn_text': 'Войти в таверну',
            'btn_color': '#ff91fb',
            'def_on_click': 'come_to_tawern',
        }]

    data = {'base_card_img_url': 'http://127.0.0.1:8000/static/img/murr_game/hell_gate.png',
            'base_card_text': text,
            'show_btn': show_btn}
    return JsonResponse(data, status=200)


def come_to_tawern(request):
    text = """\"\"\"<br>
        В последнее время в таверне море людей.<br>
        Столы ломятся от выпивки, а служанки не успевают разносить мясо и хлеб.<br><br>
        
        У барной стойки вы замечаете свободное место и ловко протискиваетесь сквозь отдыхающих.<br>
        \"\"\""""

    show_btn = [
        {
            'btb': 'show_barmen__btn',
            'btn_text': 'Поговорить с барменом',
            'btn_color': '#E8CAEB',
            'def_on_click': 'barmen',
        }]

    data = {'base_card_img_url': 'http://127.0.0.1:8000/static/img/murr_game/Tawern.png',
            'base_card_text': text,
            'show_btn': show_btn
            }
    return JsonResponse(data, status=200)


def barmen(request):
    text = """\"\"\"<br>

        Привет мой сладкий!<br>
        
        Наступают заморозки крысы ищут теплое место.<br>
        В моем подвале завелись эти мелкие твари.<br><br>
        
        Ты выглядишь достаточно крепо, что-бы разобраться с этой пакостью.<br>
        
        Я насчитал 5 штук. Принеси мне их тушки.<br>
        
        Клиентам будет спокойнее...<br>
        и обед вкуснее 😉<br>
        
        В награжу получишь мой теплый ватник (ватник +5 защита) и 1 золотой за каждую тушку.<br>
        \"\"\""""

    show_btn = [
        {
            'btb': 'show_barmen__btn',
            'btn_text': 'Поговорить с барменом',
            'btn_color': '#E8CAEB',
            'def_on_click': 'come_to_tawern',
        }
    ]

    data = {'base_card_img_url': 'http://127.0.0.1:8000/static/img/murr_game/Tawern_Barman.png',
            'base_card_text': text,
            'show_btn': show_btn
            }
    return JsonResponse(data, status=200)
