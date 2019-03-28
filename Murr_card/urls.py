from django.urls import path

from Murr_card.views import murrs_list

urlpatterns = [
    path('', murrs_list, name='murrs'),

]
