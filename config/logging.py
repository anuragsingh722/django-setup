import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RAVEN_APP = (
    'raven.contrib.django.raven_compat',
)

RAVEN_CONFIG = {
    'dsn': '<RAVEN DSN>',
}

LOGFILE = BASE_DIR + "/logs/development.log"
# disable django's default logging config and use our own config
# https://www.caktusgroup.com/blog/2015/01/27/Django-Logging-Configuration-logging_config-default-settings-logger/
LOGGING_CONFIG = None

# LOGGING
LOGGING = {
    'version': 1,
    'root': {
        'level': 'INFO',
        'handlers': ['console', 'logfile', 'sentry'],
    },
    'formatters': {
        'standard': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s : %(module)s : %(lineno)s] %(message)s  [ process: %(process)d | thread: %(thread)d]",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
    },
    'handlers': {
        'logfile': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': LOGFILE,
            'maxBytes': 1024 * 1024 * 15,  # 15MB
            'backupCount': 2,
            'formatter': 'standard',
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
        'sentry': {
            'level': 'WARNING',  # To capture more than ERROR, change to WARNING, INFO, etc.
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
            'tags': {'custom-tag': 'F23'},
        },
    },
    'loggers': {
        'raven': {
            'level': 'WARNING',
            'handlers': ['console', 'sentry', 'logfile'],
            'propagate': False,
        }
    }
}

import logging.config

logging.config.dictConfig(LOGGING)
