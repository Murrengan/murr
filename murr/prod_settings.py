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

ALLOWED_HOSTS = ['www.murrengan.ru', 'murrengan.ru', '18.216.214.27']

DEBUG = False
USE_CAPCHA = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

SECRET_KEY = '7m2tgq7yv^%^$#52%d5l_-)5ddh-lx#iu-6(u8ghx-$#of9*^$'

RECAPTCHA_PUBLIC_KEY = '6Ldb2KcUAAAAAGhi8FWFJ30BueAtEP5KGSWo9PRG'
RECAPTCHA_PRIVATE_KEY = '6Ldb2KcUAAAAAPMcBc0LiojZ8viUsoQxe94otPVd'
