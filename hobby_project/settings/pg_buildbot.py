from hobby_project.settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'hobby',
        'USER': 'hobbyuser',
        'PASSWORD': 'hobbypass',
        'HOST': '',
        'PORT': '',
    }
}

