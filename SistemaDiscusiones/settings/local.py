from .base import *

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'Discusiones',
        'USER': 'cursodjango',
        'PASSWORD': 'pass',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.child('static')]

SOCIAL_AUTH_FACEBOOK_KEY = '746259415487374'
SOCIAL_AUTH_FACEBOOK_SECRET = '36c9c25b10ac9920df5b14264e154263'

SOCIAL_AUTH_TWITTER_KEY = 'XQHq0a7nAjJTbEmKNZ3UKhDXH'
SOCIAL_AUTH_TWITTER_SECRET = '7R4sVtkklA1w7VqdTHXuShUrN51RDFaQh3AYgQ4WDhASbNFWvp'

SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
