import os

try:
    from .local_settings import *
    from captcha.constants import TEST_PUBLIC_KEY, TEST_PRIVATE_KEY

    RECAPTCHA_PUBLIC_KEY = TEST_PUBLIC_KEY
    RECAPTCHA_PRIVATE_KEY = TEST_PRIVATE_KEY
except ImportError:
    from .prod_settings import *

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # 3rd party
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'murr.spec.providers.vk',
    'tinymce',
    'crispy_forms',
    'taggit',
    'croppie',
    'captcha',
    'channels',
    'rest_framework',

    # Local
    'murr.apps.MurrConfig',
    'Murren.apps.MurrenConfig',
    'MurrCard.apps.MurrCardConfig',
    'Dashboard.apps.DashboardConfig',
    'murr_game.apps.MurrGameConfig',
    'murr_chat.apps.MurrChatConfig',
    'murr_api.apps.MurrApiConfig',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'murr.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'murr.context_processors.show_categories',
                'django.template.context_processors.csrf',
            ],
            'builtins': ['murr.templatetags.tags'],
        },
    },
]

WSGI_APPLICATION = 'murr.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = '/media/'

TINYMCE_DEFAULT_CONFIG = {
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 20,
    'selector': 'textarea',
    'theme': 'modern',
    'height': 500,
    'plugins': '''
            textcolor save link image media preview codesample contextmenu
            table code lists fullscreen  insertdatetime  nonbreaking
            contextmenu directionality searchreplace wordcount visualblocks
            visualchars code fullscreen autolink lists charmap print hr
            anchor pagebreak
            ''',
    'toolbar1': '''
            bold italic underline 
            | forecolor backcolor | bullist numlist |
            | link image media | codesample |
            ''',
    'toolbar2': '''
            visualblocks visualchars |
            charmap hr pagebreak nonbreaking anchor |  code |
            ''',
    'contextmenu': 'link image',
    'menubar': True,
    'statusbar': False,
}

CRISPY_TEMPLATE_PACK = 'bootstrap4'

# allauth

AUTH_USER_MODEL = 'Murren.Murren'

LOGIN_REDIRECT_URL = 'murr_list'
ACCOUNT_LOGOUT_REDIRECT_URL = 'murr_list'

# LOGIN_URL указываем для перенапрявления сюда пользователя, который не зарегистрирован но хочет получить доступ к
# логике, где нужно быть залогиненым. После логина направит на ожидаемую функциональность
LOGIN_URL = 'account_signup'
LOGOUT_REDIRECT_URL = 'murr_list'

ACCOUNT_FORMS = {

    'login': 'Murren.forms.CaptchaFieldLogin',
    'signup': 'Murren.forms.CaptchaFieldSignup',

}

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",

    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
)

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_UNIQUE_EMAIL = True

# //allauth


# Работа с почтой
# Для тестировани восстановления пароля на локальной машине без sendgrid
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Работаем через sendgrid
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.sendgrid.net'
# # тут менять
# EMAIL_HOST_USER = 'sendgrid_user_name'
# # и тут менять
# EMAIL_HOST_PASSWORD = 'sendgrid_password'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True

TAGGIT_CASE_INSENSITIVE = True

# murr_chat
ASGI_APPLICATION = 'murr.routing.application'

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("127.0.0.1", 6379)],
        },
    },
}

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ]
}
