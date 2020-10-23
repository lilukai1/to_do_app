"""
Django settings for to_do project.

Generated by 'django-admin startproject' using Django 3.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
     'annies-to-do-app.herokuapp.com',
     '127.0.0.1',
     'localhost',
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
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
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
                'to_do_list.context_processor.all_context'
                

            ],
        },
    },
]

WSGI_APPLICATION = 'to_do.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASE_KEY = os.environ['DATABASE_KEY']


DATABASES = {

    # 'default' : {
    # 'ENGINE': 'django.db.backends.postgresql',
    # 'HOST': 'ec2-107-20-104-234.compute-1.amazonaws.com'
    # 'DATABASE':'dd2eu7l7pf51pa'
    # 'USER': 'xtatteraczujgg'
    # 'PORT': '5432'
    # 'PASSWORD': '57b8a3bdc55d2471a58dcfa775782a47ef6d2d002ff8f994cd0fff521e8065a5'
    # 'URI': 'postgres://xtatteraczujgg:57b8a3bdc55d2471a58dcfa775782a47ef6d2d002ff8f994cd0fff521e8065a5@ec2-107-20-104-234.compute-1.amazonaws.com:5432/dd2eu7l7pf51pa'
    
    # }


        'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'wbvjvqcl',
        'HOST' : 'rajje.db.elephantsql.com',
        'USER' : 'wbvjvqcl',
        'PASSWORD' : DATABASE_KEY,
        'PORT': '5432',
    }
}

import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = BASE_DIR / 'static'

STATICFILES_DIRS = [
    BASE_DIR / 'static_files'
]

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
SIGNUP_REDIRECT_URL = '/'
AUTH_USER_MODEL = 'accounts.Account'  ## please refer to https://learndjango.com/tutorials/django-best-practices-referencing-user-model

FIXTURE_DIRS =[
    BASE_DIR / 'fixtures'
] ### python manage.py loaddata db_test.json    python manage.py dumpdata to_do_list.task > db_test.json 

## tagging settings
FORCE_LOWERCASE_TAGS = True
