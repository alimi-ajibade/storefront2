from .common import *
from dotenv import load_dotenv

load_dotenv()

DEBUG = True

SECRET_KEY = "django-insecure-hs6j037urx6iav+7#10%-vu4l4f5@@-1_zo)oft4g7$vf2$jmp"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "storefront3",
        # "HOST": "localhost",
        "HOST": "mysql",
        "USER": "root",
        "PASSWORD": "Mypassword",
    }
}

# CELERY_BROKER_URL = "redis://localhost:6379/1"
CELERY_BROKER_URL = "redis://redis:6379/1"

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        # "LOCATION": "redis://127.0.0.1:6379/2",
        "LOCATION": "redis://redis:6379/2",
        "TIMEOUT": 10 * 60,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    }
}

# This value for EMAIL_BACKEND is used in django by defualt
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = "localhost"
# for docker
EMAIL_HOST = "smtp4dev"
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""
EMAIL_PORT = 2525

# Hack to enable debug toolbar run in docker environment
DEBUG_TOOLBAR_CONFIG = {"SHOW_TOOLBAR_CALLBACK": lambda request: True}
