from django.urls import path

from .views import murr_ui

urlpatterns = [
    path('', murr_ui, name='murr_ui'),

]
