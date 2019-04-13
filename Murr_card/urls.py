from django.urls import path

from Murr_card.views import murrs_list, murr_detail, search, murr_update, murr_delete, murr_create

urlpatterns = [
    path('', murrs_list, name='murrs_list'),
    path('murrs_by_tag/<str:tag_name>', murrs_list, name='murrs_list_by_tag_name'),
    path('create/', murr_create, name='murr_create'),
    path('murr_detail/<int:pk>', murr_detail, name='murr_detail'),
    path('murr_detail/<int:pk>/update/', murr_update, name='murr_update'),
    path('murr_detail/<int:pk>/delete/', murr_delete, name='murr_delete'),
    path('search/', search, name='search'),
]
