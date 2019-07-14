from django.db import models
from django.contrib.auth import get_user_model


class MurrChatName(models.Model):
    group_name = models.CharField(max_length=255, default='')

    @property
    def link(self):
        channel_name = self.channel_name(self.id)
        return f'/ws/chat/{channel_name}/'

    def __str__(self):
        return self.group_ndame

    @classmethod
    def channel_name(cls, group_id):
        return f'{group_id}'


class MurrChatMembers(models.Model):
    user = models.ForeignKey(get_user_model(), related_name='murr_chat_user', on_delete=models.CASCADE, null=True)
    group = models.ForeignKey(MurrChatName, related_name='murr_group_member', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.user.username


class MurrChatMessage(models.Model):
    user = models.ForeignKey(get_user_model(), related_name='murren_message', on_delete=models.CASCADE, null=True)
    group = models.ForeignKey(MurrChatName, related_name='murr_group_message', on_delete=models.CASCADE, null=True)
    message = models.TextField(default='')

    def __str__(self):
        return self.message
