import json

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import get_user_model
# from murr_game.engine.mock import User
from murr_game.engine.mock import Opponent
from django.http import JsonResponse

from murr_game.engine.actions import Actions
from murr_game.engine.character import CharacterEngine
from django.forms.models import model_to_dict

from murr_game.engine.stats import Stats
# from murr_game.models import Character
#
User = get_user_model()


@login_required
def murr_game(request):

    murren = User.objects.get(username=request.user.username)

    context = {
        'murren': murren
    }
    return render(request, 'murr_game/murr_game.html', context=context)
#
#
# @login_required
# def return_members(request):
#     character, created = Character.objects.get_or_create(name=request.user.username, actions='actions', stats='stats')
#     character_engine = CharacterEngine(character, Actions, Stats, base_class='weapon')
#     character = model_to_dict(character)
#     character.update({'actions': character_engine.actions, 'stats': character_engine.stats})
#
#     common_opponent = CharacterEngine(Opponent, Actions, Stats, base_class='magic')
#     opponent = {}
#     opponent.update({'actions': common_opponent.actions, 'name': common_opponent.name, 'stats': common_opponent.stats})
#
#     data = {}
#     data.update({'character': character, 'opponent': opponent})
#
#     return JsonResponse(data, status=200)
#
#
# @login_required
# def return_character_info(request):
#     character, created = Character.objects.get_or_create(name=request.user.username, actions='actions', stats='stats')
#     character_engine = CharacterEngine(character, Actions, Stats, base_class='weapon')
#
#     character = model_to_dict(character)
#     character.update({'actions': character_engine.actions, 'stats': character_engine.stats})
#
#     avatar = User.objects.get(id=request.user.id)
#     avatar_url = avatar.profile_picture.url
#
#     data = {}
#     data.update({'character': character, 'avatar_url': avatar_url, 'user_id': request.user.id})
#     return JsonResponse(data, status=200)
