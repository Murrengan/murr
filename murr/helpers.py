import os
import platform
import shutil
from django.contrib.auth import get_user_model

from murr_chat.models import MurrChatName

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAKE_MIGRATIONS = 'python manage.py makemigrations murr_game murr_chat MurrCard Murren'

MIGRATE = 'python manage.py migrate'


class BaseProcessor:
    MODEL = None

    def __init__(self, data):
        self._raw = data
        self.params = {}
        self.errors = {}
        self._instance = None
        self._processed_field = None

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
            method_name = f'_process_{field.name}'
            method = getattr(self, method_name, lambda: None)
            self._processed_field = field.name
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
        field = field or self._processed_field
        self.errors[field] = message


def delete_db_and_migrations():
    system = platform.system()
    if system == 'Windows':
        separator = '\\'
    else:
        separator = '/'

    prepare_for_delete = []
    for dirname, dirnames, filenames in os.walk(BASE_DIR):
        if 'db.sqlite3' in filenames:
            db_path = BASE_DIR + separator + 'db.sqlite3'
            os.remove(db_path)
        for subdirname in dirnames:
            if '.git' in dirnames:
                dirnames.remove('.git')
            if 'migrations' in subdirname:
                prepare_for_delete.append(os.path.join(dirname, subdirname))

    for i in prepare_for_delete:
        shutil.rmtree(i, ignore_errors=True)


def create_superuser():
    user = get_user_model()
    user.objects.create_superuser('Greg', '', 'Greg')


def group_create(group_name):
    group = MurrChatName(group_name=group_name)
    group.save()
