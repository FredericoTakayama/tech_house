# -*- coding: utf-8 -*-
from django.conf import settings
# ou: from settings import *

# print('entrou no settings production!')

import os
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # mudar para mysql em modo de produção, para o rasp coletar infos
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'), # path do arquivo do banco
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}