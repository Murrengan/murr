from django.urls import path

from .views import mg_engine

urlpatterns = [
    path('', mg_engine, name='mg_engine')

]
