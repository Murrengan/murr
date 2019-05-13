from django.urls import path

from . import views as murren

urlpatterns = [
    path('follow/', murren.follow, name='murren_follow'),
    path('unfollow/', murren.unfollow, name='murren_unfollow'),
    path('show_all_liked_murrs/', murren.show_all_liked_murrs, name='show_all_liked_murrs'),
    path('<str:username>/', murren.profile, name='murren_profile'),
]
