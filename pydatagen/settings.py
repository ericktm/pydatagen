import os
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS

PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Erick Roberto de Oliveira', 'contato@erick.net.br'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'pydatagen',  # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'pydatagen',
        'PASSWORD': 'py123gen',
        'HOST': 'localhost',  # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '5432',  # Set to empty string for default.
    }
}

ALLOWED_HOSTS = []

TIME_ZONE = 'America/Cuiaba'
LANGUAGE_CODE = 'pt-BR'

SITE_ID = 1
USE_I18N = True
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = False

MEDIA_ROOT = PROJECT_PATH + '/media/'

MEDIA_URL = '/media/'

STATIC_ROOT = 'static'

STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    PROJECT_PATH + '/static/',
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'xk%_)g0n9=g)-m#dd-#j#y$r=f$x4fxtxs%j-57tg2i=3o8@_^'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'pydatagen.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'pydatagen.wsgi.application'

TEMPLATE_DIRS = (
    PROJECT_PATH + '/templates/',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'kronos',
    # 'south',
    'app',
    'gunicorn',
)

TEMPLATE_CONTEXT_PROCESSORS += (
    'django.core.context_processors.request',
)

SQL_DIR = os.path.join(PROJECT_PATH, 'media/project_files')