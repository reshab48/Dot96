from .base import *

DEBUG = False

ALLOWED_HOSTS = ['admin.dot96.com']

ADMINS = (
	('Reshab Das', 'das.reshab48@gmail.com'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
)

ROOT_URLCONF = 'dot96.admin_urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'dot96.admin_wsgi.application'

DATABASES = {
	'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'Dot96',
        'USER': 'webadmin',
        'PASSWORD': 'QJLy7S9QJ2',
        'HOST': '192.168.100.200',
        'PORT': '5432',
	}
}