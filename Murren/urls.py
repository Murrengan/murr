from django.urls import path

from . import views

urlpatterns = [
    path('follow/', views.follow, name='murren_follow'),
    path('unfollow/', views.unfollow, name='murren_unfollow'),
]
