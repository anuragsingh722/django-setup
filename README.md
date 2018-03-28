**Getting Started**

Installation requirements
`https://docs.djangoproject.com/en/2.0/topics/install/`

Start a project
`https://docs.djangoproject.com/en/2.0/intro/tutorial01/`

Set up instructions reference
`https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04`


Quick reference to commands


1. Setting up a new project
```
django-admin startproject projectname
```


2. Create a logging configuration

- Create a `logging.py` inside `projectname\projectname`. Use the following config to set up logging.

```
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
```
- Import this file inside `projectname\projectname\settings.py`.
```
try:
    from .logging import *
except ImportError:
    pass
```


3. Create a database configuration (*if required. A stateless service doesn't require a database setup.)
- Create a `database.py` inside `projectname\projectname`. Move the following code from `projectname\projectname\settings.py` to `projectname\projectname\database.py`.
  You can configure this file to use database of your choice. The following configuration is for postgres on a local machine. For reference checkout `https://docs.djangoproject.com/en/1.11/ref/settings/#databases`.
```
# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django_tenants.postgresql_backend',
        'NAME': '<DBNAME>',
        'USER': '<USER>',
        'PASSWORD': '<PASSWORD>',
        'HOST': '<HOST>'
    }
}
```
- Import this file inside `projectname\projectname\settings.py`.
```
try:
    from .database import *
except ImportError:
    pass
```
4. To run the server
`python manage.py runserver`


