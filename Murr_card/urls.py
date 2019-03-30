from django.urls import path

from Murr_card.views import murrs_list, murr_detail, search

urlpatterns = [
    path('', murrs_list, name='murrs_list'),
    path('murr_detail/<int:pk>', murr_detail, name='murr_detail'),
    path('search/', search, name='search'),

]
