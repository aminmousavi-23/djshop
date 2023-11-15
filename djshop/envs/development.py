from .common import *

ALLOWED_HOSTS = ['*']

INSTALLED_APPS  =  [
   'drf_spectacular',
] + INSTALLED_APPS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'djshop',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'hamilton23'
    }
}

LOGGING = {
    'version': 1,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.db.backends': {
            'level': 'DEBUG',
        },
    },
    'root': {
        'handlers': ['console'],
    }
}