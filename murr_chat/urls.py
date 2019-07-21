from django.urls import path

from murr_chat.views import murr_chat

urlpatterns = [
    path('', murr_chat, name='murr_chat')
]
