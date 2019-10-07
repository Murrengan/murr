from django.urls import path, include

from .views import *

urlpatterns = [

    path('murrens_list/', MurrenList.as_view()),
    path('get_murren_data/<int:pk>/', MurrenById.as_view()),

    path('get_all_murrs/', MurrList.as_view(), name='get_all_murrs'),
    path('murr_detail/<str:pk>', MurrDetail.as_view(), name='api_murr_detail'),

    # # token authentication
    # path('rest-auth/', include('rest_auth.urls')),
    # path('rest-auth/registration/', include('rest_auth.registration.urls')),

    # murr_game
    path('start/', start),
    path('look_at_hell_gate/', look_at_hell_gate),
    path('come_to_tawern/', come_to_tawern),
    path('barmen/', barmen),
]
