import environ
from .base import *

env = environ.Env()
environ.Env.read_env()

SECRET_KEY = os.environ.get("SECRET_KEY")

DEBUG = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': os.environ.get("DB_ENGINE", "django.db.backends.sqlite3"),
        'NAME': os.environ.get("DB_NAME", os.path.join(BASE_DIR, "db.sqlite3")),
    }
}
