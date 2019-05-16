from django.urls import path

from .views import dashboard

urlpatterns = [
    path('', dashboard, name='dashboard'),
    # path('show_category/', show_category, name='show_category'),
]
