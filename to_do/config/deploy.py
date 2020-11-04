import dj_database_url

DEBUG = False
DATABASES = {
        'default': {
    }
}

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

db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)


django_heroku.settings(locals())