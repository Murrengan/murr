from django.urls import path

from MurrCard.views import *

urlpatterns = [
    path('', murr_list, name='murr_list'),
    path('simple_search', simple_search, name='simple_search'),
    path('like/', like, name='like'),
    path('unlike/', unlike, name='unlike'),
    path('create/', murr_create, name='murr_create'),
    # murr_detail under construction: нужно переверстать старый шаблон с учетом новых инклюдови и апи вьъх
    path('murr_detail/<str:slug>', murr_detail, name='murr_detail'),
    path('murr_detail/<str:slug>/update/', murr_update, name='murr_update'),
    path('murr_detail/<str:slug>/delete/', murr_delete, name='murr_delete'),
    path('comment_add/', comment_add, name='comment_add'),
    path('comment_delete/', comment_delete),
    path('comment_edit/', comment_edit),
    path('comment_update/', comment_update),
    path('murr_action/', murr_action)

]
