from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3be)qjchi@n8+2ly5@jb@8nzxdgrf&^yb(f_^=rbhi0a^j*g=6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
