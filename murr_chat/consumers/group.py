from channels.db import database_sync_to_async
from django.contrib.auth import get_user_model

from murr_chat.models import MurrChatMembers, MurrChatName

from .base import MurrChatConsumer


class GroupChatConsumer(MurrChatConsumer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.channel = None

    async def connect(self):
        await super().connect()
        self.channel = MurrChatName.user_channel_name(self.scope['user'].id)
        await self.channel_layer.group_add(self.channel, self.channel_name)

    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.channel, self.channel_name)
        await super().disconnect(code=code)

    async def send_notice(self, event):
        await self._send_message(event['data']['data'], event=event['data']['event'])

    async def event_group_list(self, event):
        data = await self.group_list(self.scope['user'])
        await self._send_message(data, event=event['event'])

    async def event_user_list(self, event):
        data = await self.user_list(self.scope['user'])
        await self._send_message(data, event=event['event'])

    async def event_group_create(self, event):
        name = event['data'].get('name')
        if not name:
            return await self._trow_error({'detail': 'Missing group name'}, event=event['event'])
        data = await self.group_create(name, self.scope['user'])
        if data.get('error'):
            await self._trow_error(data, event=event['event'])
        await self._send_message(data, event=event['event'])

    @database_sync_to_async
    def group_list(self, user):
        groups_ids = list(MurrChatMembers.objects.filter(user=user).values_list('group', flat=True))
        result = []
        for group in MurrChatName.objects.filter(id__in=groups_ids):
            result.append({
                'id': group.id,
                'group_name': group.group_name,
                'link': group.link
            })
        return result

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

    @database_sync_to_async
    def group_create(self, group_name, user):
        group = MurrChatName(group_name=group_name)
        group.save()
        group_member = MurrChatMembers(group=group, user=user)
        group_member.save()
        return {'id': group.id, 'name': group.group_name, 'link': group.link}
