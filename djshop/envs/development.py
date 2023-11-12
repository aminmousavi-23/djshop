from .common import *

ALLOWED_HOSTS = ['*']

INSTALLED_APPS  =  [
   
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