from django.urls import path

from .views import murren_profile

urlpatterns = [
    path('<str:username>/', murren_profile, name='murren_profile')

]
