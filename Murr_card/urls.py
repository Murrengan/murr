from django.urls import path
from Murr_card.views import murrs_list, murr_detail, search, murr_update, murr_delete, murr_create, comment_cut

from Murr_card.views import murr_list, murr_detail, search, murr_update, murr_delete, murr_create, comment_cut


urlpatterns = [
    path('', murr_list, name='murr_list'),
    path('murrs_by_tag/<str:tag_name>', murr_list, name='murr_list_by_tag_name'),
    path('create/', murr_create, name='murr_create'),
    path('murr_detail/comment_cut.ajax/<int:id>/', comment_cut, name='comment_cut.ajax'),
    path('murr_detail/<str:slug>', murr_detail, name='murr_detail'),
    path('murr_detail/<str:slug>/update/', murr_update, name='murr_update'),
    path('murr_detail/<str:slug>/delete/', murr_delete, name='murr_delete'),
    path('search/', search, name='search'),
]
