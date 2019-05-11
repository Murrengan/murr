from django.urls import path
from MurrCard import views as murr_card

urlpatterns = [
    path('', murr_card.murr_list, name='murr_list'),
    path('like/', murr_card.like, name='like'),
    path('unlike/', murr_card.unlike, name='unlike'),
    path('murrs_by_tag/<str:tag_name>', murr_card.murr_list, name='murr_list_by_tag_name'),
    path('create/', murr_card.murr_create, name='murr_create'),
    path('murr_detail/comment_cut.ajax/<int:pk>/', murr_card.comment_cut, name='comment_cut.ajax'),
    path('murr_detail/comment_edit.ajax/<int:pk>/', murr_card.comment_edit, name='comment_edit.ajax'),
    path('murr_detail/<str:slug>', murr_card.murr_detail, name='murr_detail'),
    path('murr_detail/<str:slug>/update/', murr_card.murr_update, name='murr_update'),
    path('murr_detail/<str:slug>/delete/', murr_card.murr_delete, name='murr_delete'),
    path('search/', murr_card.search, name='search'),
]
