from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import get_user_model
# from murr_game.engine.mock import User
from murr_game.engine.mock import Opponent
from django.http import JsonResponse

from murr_game.engine.actions import Actions
from murr_game.engine.character import CharacterEngine
from django.forms.models import model_to_dict
from murr_game.models import Character

User = get_user_model()


@login_required
def murr_game(request):
    return render(request, 'murr_game/murr_game.html')


@login_required
def return_members(request):
    character, created = Character.objects.get_or_create(name=request.user.username, actions='actions')
    character_engine = CharacterEngine(character, Actions, base_class='weapon')

    character = model_to_dict(character)
    character.update({'actions': character_engine.actions})

    common_opponent = CharacterEngine(Opponent, Actions, base_class='magic')
    opponent = {}

    opponent.update({'actions': common_opponent.actions, 'name': common_opponent.name})

    data = {}
    data.update({'character': character})
    data.update({'opponent': opponent})

    return JsonResponse(data, status=200)
