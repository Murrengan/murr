from django.contrib.auth import get_user_model

from murr.helpers import BaseProcessor
from murr.shortcuts import parse_int
from .models import Like, Murr

User = get_user_model()


class LikeProcessor(BaseProcessor):
    MODEL = Like

    def _process_murren(self):
        pk = parse_int(self._raw.get('murren'))
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            self._err('incorrect murren id')

    def _process_murr(self):
        slug = self._raw.get('murr')
        try:
            return Murr.objects.get(slug=slug)
        except User.DoesNotExist:
            self._err('incorrect murr id')
