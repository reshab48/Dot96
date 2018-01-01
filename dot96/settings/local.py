from .base import *

DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'shop',
    'sorl.thumbnail',
    'cart',
    'account',
    'django.contrib.admin',
)

ROOT_URLCONF = 'dot96.urls'

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
                'shop.context_processors.sub_categories',
                'shop.context_processors.categories',
                'shop.context_processors.items_viewed',
                'cart.context_processors.cart',
            ],
        },
    },
]

WSGI_APPLICATION = 'dot96.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

ABSOLUTE_URL_OVERRIDES = {
    'auth.user' : lambda u: reverse_lazy('account:account_detail', args=[u.username]),
}

VIEW_SESSION_ID = 'items_viewed'
CART_SESSION_ID = 'cart'

LOGIN_REDIRECT_URL = reverse_lazy('shop:index')
LOGIN_URL = reverse_lazy('account:login')
LOGOUT_URL = reverse_lazy('account:logout')