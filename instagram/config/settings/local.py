import random
import string
import logging
logger = logging.getLogger(__name__)

from .base import *

DEBUG = False


ALLOWED_HOSTS = [
    '.elasticbeanstalk.com'
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
    }

}

SECRET_KEY = ''.join(
    [random.choice(string.ascii_lowercase) for i in range(40)]
)

LOGGING = {
    'version': 1,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(ROOT_DIR, '.log', 'django.log')
        },
    },
    'loggers': {
        'django': {
            'handlers': [
                'console',
                'file',
            ],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}