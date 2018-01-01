from .base import *

DEBUG = False

GOOGLE_RECAPTCHA_SECRET_KEY = '6LeswzoUAAAAAAHe1484Yhxz5-y3p9NCiMh61iD7'

ALLOWED_HOSTS = ['dot96.com', 'www.dot96.com']

ADMINS = (
	('Reshab Das', 'das.reshab48@gmail.com'),
)

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
)

ROOT_URLCONF = 'dot96.user_urls'

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

WSGI_APPLICATION = 'dot96.user_wsgi.application'

DATABASES = {
	'default': {
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