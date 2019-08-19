from django.urls import path

from murr_chat.consumers.group import GroupChatConsumer
from .consumers.chat import ChatConsumer


websocket_urls = [

    path('ws/chat/', GroupChatConsumer),
    path('ws/chat/<str:group_id>/', ChatConsumer)

]
