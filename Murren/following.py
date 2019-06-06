from django.contrib.auth import get_user_model

from murr.helpers import BaseProcessor
from murr.shortcuts import parse_int
from .models import Following

User = get_user_model()


class FollowingProcessor(BaseProcessor):
    MODEL = Following

    def _process_follower(self):
        pk = parse_int(self._raw.get('follower'))
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            self._err('incorrect follower id')

    def _process_master(self):
        pk = parse_int(self._raw.get('master'))
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            self._err('incorrect master id')
