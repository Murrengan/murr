import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'murrengan_bd',
        'USER': 'murren',
        'PASSWORD': 'murrengan',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

ALLOWED_HOSTS = ['murrengan.ru', '18.216.214.27']

DEBUG = False

SECRET_KEY = '7m2tgq7yv^%^$#52%d5l_-)5ddh-lx#iu-6(u8ghx-$#of9*^$'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
