from django.urls import path
from .views import MurrenList, MurrenById

urlpatterns = [
    path('murrens_list/', MurrenList.as_view()),
    path('murren_by_pk/<int:pk>/', MurrenById.as_view()),
]
