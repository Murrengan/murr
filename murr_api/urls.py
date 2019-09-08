from django.urls import path

from .views import MurrenList, MurrenById, start, MurrList, MurrDetail

urlpatterns = [
    path('murrens_list/', MurrenList.as_view()),
    path('murren_by_pk/<int:pk>/', MurrenById.as_view()),
    path('start/', start),

    path('get_all_murrs/', MurrList.as_view(), name='get_all_murrs'),
    path('murr_detail/<str:pk>', MurrDetail.as_view(), name='api_murr_detail'),
]
