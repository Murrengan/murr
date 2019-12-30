from django.urls import path
from .views import MurrensMethods


urlpatterns = [
    path('', MurrensMethods.as_view(), name='MurrensMethods'),

]
