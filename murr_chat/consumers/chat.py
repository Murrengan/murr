from channels.db import database_sync_to_async
from django.contrib.auth import get_user_model

from murr_chat.models import MurrChatName, MurrChatMembers, MurrChatMessage
from .base import MurrChatConsumer


class GroupConsumer(MurrChatConsumer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.group_id = self.scope['url_route']['kwargs']['group_id']
        self.group = None
        self.chat_members = []
        self.channel = f'group_id_{self.group_id}'

    async def connect(self):
        await super().connect()
        group = await self.get_group()
        if not group:
            await self._trow_error({'detail': 'Group not found'})
            await self.close()
            return

        # Приватные группы
        # chat_members = await self.get_chat_members()
        # if group_type is privete:
        #     if self.scope['user'].id not in chat_members:
        #         await self._trow_error({'detail': 'Access denied'})
        #         await self.close()
        #         return
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

    async def event_murren_in_tawern_list(self, event):
        data = await self.user_list(self.scope['user'])
        await self._send_message(data, event=event['event'])

    async def event_add_chat_member(self, event):
        user_id = event['data'].get('user_id')
        if not user_id:
            return await self._trow_error({'detail': 'Missing user id'}, event=event['event'])
        await self.add_chat_member(user_id)
        chat_members = await self.get_chat_members()
        return await self._send_message(chat_members, event=event['event'])

    async def event_leave_group(self, event):
        user_id = self.scope['user'].id
        log = await self.remove_chat_member(user_id)
        group_members = await self.get_chat_members()
        await self._send_message({'log': log, 'group_members': group_members}, event=event['event'])
        await self.close(code=1000)

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
    def remove_chat_member(self, user_id):
        user = get_user_model().objects.filter(id=user_id).first()
        log = ''
        if user:
            answer = MurrChatMembers.objects.filter(user=user_id).delete()[0]
            if answer:
                log = 'Муррен удален из группы'
            else:
                log = 'Ошибка удаления или 0'
        return log


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

    @database_sync_to_async
    def user_list(self, user):
        users = get_user_model().objects.all().exclude(pk=user.id)
        result = []
        for user in users:
            result.append({
                'id': user.id,
                'username': user.username,
                'email': user.email
            })
        return result
