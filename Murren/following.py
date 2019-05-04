from django.contrib.auth import get_user_model

from .models import Following
from murr.shortcuts import parse_int

User = get_user_model()


class FollowingProcessor:
    MODEL = Following

    def __init__(self, data):
        self._raw = data
        self.params = {}
        self.errors = {}
        self._instance = None
        self._process_field = None

    def process(self):
        self._process()
        self._post_process()
        self._instance = self._get_instance()

    def save(self):
        self._instance.save()

    def delete(self):
        if self._instance.pk:
            self._instance.delete()

    def _process(self):
        for field in self._get_fields():
            method = getattr(self, f'_process_{field.name}', lambda: None)
            self._process_field = field.name
            self.params[field.name] = method()

    def _post_process(self):
        pass

    def _get_fields(self):
        fields = []
        for field in self.MODEL._meta.fields:
            if field.name != 'id' or self._raw.get('id'):
                fields.append(field)
        return fields

    def _get_instance(self):
        try:
            return self.MODEL.objects.get(**self.params)
        except self.MODEL.DoesNotExist:
            return self.MODEL(**self.params)

    def _err(self, message, field=None):
        field = field or self._process_field
        self.errors[field] = message

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
