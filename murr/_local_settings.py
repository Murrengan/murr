import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

ALLOWED_HOSTS = []

DEBUG = True

SECRET_KEY = '7m2tgq7yv^%^$#52%d5l_-)5ddh-lx#iu-6(u8ghx-$#of9*^$'


STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]
