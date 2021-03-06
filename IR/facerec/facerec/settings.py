"""
Django settings for facerec project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
SETTINGS_DIR = os.path.dirname(__file__)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
TEMPLATE_PATH = os.path.join(BASE_DIR, 'templates')
DATABASE_PATH = os.path.join(BASE_DIR, 'droidapp.db')
ADMIN_MEDIA_PREFIX='/static/'
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_*j)d94$84f^v4)f-k_1tquu5x@&8$vsp1ej4y_9kf9ug+i61u'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []
DEFAULT_FROM_EMAIL = "Coding For Entrepreneurs <codingforentrepreneurs@gmail.com>"

try:
    from .email_settings import host, user, password
    EMAIL_HOST = host #"smtp.gmail.com" #"smtp.sendgrid.net"
    EMAIL_HOST_USER = user #"codingforentrepreneurs@gmail.com"
    EMAIL_HOST_PASSWORD = password #"password"
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
except:
    pass

SITE_URL = "http://cfestore.com"

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'droidapp',
    'jobs',
    'haystack',
    'accounts',
    'carts',
    'marketing',
    'orders',
    'products',
    'localflavor',
)

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
        'URL': 'http://127.0.0.1:8983/solr'
    },
}

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'marketing.middleware.DisplayMarketing',
)

ROOT_URLCONF = 'facerec.urls'

WSGI_APPLICATION = 'facerec.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': DATABASE_PATH,
    }
}

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    TEMPLATE_PATH,
)
# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True
MARKETING_HOURS_OFFSET = 3
MARKETING_SECONDS_OFFSET = 0
DEFAULT_TAX_RATE = 0.08 # 8%


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_PATH = os.path.join(BASE_DIR,'static')

STATIC_URL = '/static/' # You may find this is already defined as such.

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static", "media")
#MEDIA_ROOT = '/Users/jmitch/Desktop/ecommerce/static/media/'

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static", "static_root")

STATICFILES_DIRS = (
    os.path.join(os.path.dirname(BASE_DIR), "static", "static_files"),
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)


STRIPE_SECRET_KEY = "sk_test_tXCtSORPdz4nrozcoOsiCy2A"
STRIPE_PUBLISHABLE_KEY = "pk_test_giqz4Y9dhjdg6QtIUbuOBahj"
