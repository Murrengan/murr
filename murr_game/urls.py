from django.urls import path

from murr_game.views import murr_game, return_members

urlpatterns = [
    path('', murr_game, name='murr_game'),

    # api
    path('api/return_members/', return_members, name='return_members')
]
