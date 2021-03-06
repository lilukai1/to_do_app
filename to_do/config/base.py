"""
Django settings for to_do project.

Generated by 'django-admin startproject' using Django 3.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import django_heroku

BASE_DIR = Path(__file__).resolve().parent.parent


ALLOWED_HOSTS = [
     'annies-to-do-app.herokuapp.com',
     '127.0.0.1',
     'localhost',
     'coderannie.com',
     'transparent-firefly-9qyjzvy95zh643n2e2jxxjyl.herokudns.com',
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'to_do_list',
    'accounts',
    'crispy_forms',   
    'debug_toolbar',
    'psmf_calculator',
    'resume', 
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'to_do.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ BASE_DIR / 'templates'

        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'to_do_list.context_processor.all_context',
            
            ],
        },
    },
]

WSGI_APPLICATION = 'to_do.wsgi.application'


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [
    BASE_DIR / 'static'
]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

LOGIN_REDIRECT_URL = "/to_do/index/"
LOGOUT_REDIRECT_URL = "/to_do/index/"
SIGNUP_REDIRECT_URL = "/to_do/index/"
AUTH_USER_MODEL = 'accounts.Account'  ## please refer to https://learndjango.com/tutorials/django-best-practices-referencing-user-model

FIXTURE_DIRS =[
    BASE_DIR / 'fixtures'
] ### python manage.py loaddata db_test.json    python manage.py dumpdata to_do_list.task > db_test.json 

## tagging settings
# FORCE_LOWERCASE_TAGS = True

