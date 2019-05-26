from django.urls import path

from . import views as murren

urlpatterns = [
    path('follow/', murren.follow, name='murren_follow'),
    path('unfollow/', murren.unfollow, name='murren_unfollow'),
    path('<str:username>/', murren.profile, name='murren_profile'),
]
