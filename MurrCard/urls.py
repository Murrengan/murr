from django.urls import path

from MurrCard import views as murr_card

urlpatterns = [
    path('', murr_card.murr_list, name='murr_list'),
    path('like/', murr_card.like, name='like'),
    path('unlike/', murr_card.unlike, name='unlike'),
    path('murrs_by_tag/<str:tag_name>', murr_card.murr_list, name='murr_list_by_tag_name'),
    path('murrs_by_category/<str:category>', murr_card.murr_list, name='murr_list_by_category'),
    path('create/', murr_card.murr_create, name='murr_create'),
    # murr_detail under construction: нужно переверстать старый шаблон с учетом новых инклюдови и апи вьъх
    # path('murr_detail/<str:slug>', murr_card.murr_detail, name='murr_detail'),
    # path('murr_detail/<str:slug>/update/', murr_card.murr_update, name='murr_update'),
    # path('murr_detail/<str:slug>/delete/', murr_card.murr_delete, name='murr_delete'),
    path('comment_add/', murr_card.comment_add),
    path('comment_delete/', murr_card.comment_delete),
    path('comment_edit/', murr_card.comment_edit),
    path('comment_update/', murr_card.comment_update),
    path('search/', murr_card.search, name='search'),
]

