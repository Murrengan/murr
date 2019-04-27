from django.urls import path

from . import views

urlpatterns = [
    path('<str:username>', views.profile, name='murren_profile'),
    path('<str:username>/follow/', views.follow, name='murren_follow')
]
