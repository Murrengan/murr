from django.db.models.signals import post_save
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

from .models import MurrChatMembers, MurrChatMessage, MurrChatName


def send_chat_message(data, channel_name):
    async_to_sync(get_channel_layer().group_send)(channel_name, data)


def new_group(sender, instance, created, **kwargs):
    if created:
        first_member = MurrChatMembers.objects.filter(group=instance.group).order_by('id').first()
        if first_member.user.id != instance.user.id:
            data = {
                'type': 'send.notice',
                'data': {
                    'event': 'new.group',
                    'data': {
                        'id': instance.group.id,
                        'name': instance.group.group_name,
                        'link': instance.group.link,
                    }

                }
            }
            channel_name = MurrChatName.user_channel_name(instance.user.id)
            send_chat_message(data, channel_name)


def new_message(sender, instance, created, **kwargs):
    if created:
        data = {
            'type': 'send.notice',
            'data': {
                'event': 'new.message',
                'data': {
                    'id': instance.id,
                    'group_id': instance.group.id,
                    'message': instance.message,
                }

            }
        }
        members = MurrChatMembers.objects.filter(group=instance.group).exclude(user=instance.user)
        for member in members:
            channel_name = MurrChatName.user_channel_name(member.user.id)
            send_chat_message(data, channel_name)


post_save.connect(new_group, sender=MurrChatMembers, dispatch_uid='new_group_member')
post_save.connect(new_message, sender=MurrChatMessage, dispatch_uid='new_group_message')
