from channels.db import database_sync_to_async
from django.contrib.auth import get_user_model

from murr_chat.models import MurrChatName, MurrChatMembers, MurrChatMessage
from .base import MurrChatConsumer


class ChatConsumer(MurrChatConsumer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.group_id = self.scope['url_route']['kwargs']['room_name']
        self.group = None
        self.chat_members = []
        self.channel = f'group_{self.group_id}'

    async def connect(self):
        await super().connect()
        group = await self.get_group()
        if not group:
            await self._trow_error({'detail': 'Group not found'})
            await self.close()
            return
        chat_members = await self.get_chat_members()
        if self.scope['user'].id not in chat_members:
            await self._trow_error({'detail': 'Access denied'})
            await self.close()
            return
        await self.channel_layer.group_add(self.channel, self.channel_name)

    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.channel, self.channel_name)
        await super().disconnect(code=code)

    async def event_send_message(self, event):
        message = event['data'].get('message')
        if not message:
            return await self._trow_error({'detail': 'Missing message'}, event=event['event'])
        await self.save_message(message, self.scope['user'])
        data = {
            'username': self.scope['user'].username,
            'message': event['data']['message']

        }
        return await self._group_send(data, event=event['event'])

    async def event_list_messages(self, event):
        messages = await self.get_messages()
        return await self._send_message(messages, event=event['event'])

    async def event_add_chat_member(self, event):
        user_id = event['data'].get('user_id')
        if not user_id:
            return await self._trow_error({'detail': 'Missing user id'}, event=event['event'])
        await self.add_chat_member(user_id)
        chat_members = await self.get_chat_members()
        return await self._send_message(chat_members, event=event['event'])

    @database_sync_to_async
    def get_group(self):
        group = MurrChatName.objects.filter(id=self.group_id).first()
        if group:
            self.group = group
        return group

    @database_sync_to_async
    def get_chat_members(self):
        chat_members = list(MurrChatMembers.objects.filter(group=self.group).values_list('user', flat=True))
        self.chat_members = chat_members
        return chat_members

    @database_sync_to_async
    def add_chat_member(self, user_id):
        user = get_user_model().objects.filter(id=user_id).first()
        if user:
            chat_member, _ = MurrChatMembers.objects.get_or_create(group=self.group, user=user)

    @database_sync_to_async
    def save_message(self, message, user):
        m = MurrChatMessage(user=user, group=self.group, message=message)
        m.save()

    @database_sync_to_async
    def get_messages(self):
        messages = MurrChatMessage.objects.select_related('user').filter(group=self.group).order_by('id')
        res = []
        for message in messages:
            res.append({
                'id': message.id,
                'username': message.user.username,
                'message': message.message
            })
        return res
