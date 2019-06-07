from django.contrib.auth import get_user_model

from .models import MurrAction, Murr
from murr.shortcuts import parse_int
from murr.helpers import BaseProcessor

User = get_user_model()


class ActionProcessor(BaseProcessor):
    MODEL = MurrAction

    def _process_murren(self):
        pk = parse_int(self._raw.get('murren'))
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            self._err('incorrect murren id')

    def _process_murr(self):
        pk = self._raw.get('murr')
        try:
            return Murr.objects.get(pk=pk)
        except User.DoesNotExist:
            self._err('incorrect murr id')

    def _process_action(self):
        action = self._raw.get('action')
        return action
