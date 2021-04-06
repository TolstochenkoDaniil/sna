import os
import environ
from pathlib import Path

env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = env('SECRET_KEY', cast=str, default='sup3r_53cr3t_p@ssw0rd')

DEBUG = env('DEBUG', cast=bool, default=False)
CLOUD = env('CLOUD', cast=bool, default=False)

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'crispy_forms',

    'registration',
    'user_stats'
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'sna.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(BASE_DIR.joinpath('templates'))],
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

WSGI_APPLICATION = 'sna.wsgi.application'

if CLOUD and DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': env('DB_ENGINE', cast=str, default='django.db.backends.mysql'),
            'PORT': env('DB_PORT', cast=str),
            'HOST': '127.0.0.1',
            'USER': env('DB_USER', cast=str),
            'PASSWORD': env('DB_PASSWORD', cast=str),
            'NAME': env('DB_NAME', cast=str),
        }
    }
elif DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': env('DB_ENGINE', cast=str, default='django.db.backends.mysql'),
            'HOST': '/cloudsql/{}'.format(env('DB_HOST', cast=str)),
            'USER': env('DB_USER', cast=str),
            'PASSWORD': env('DB_PASSWORD', cast=str),
            'NAME': env('DB_NAME', cast=str),
        }
    }

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

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILESDIRS = (os.path.join(BASE_DIR, 'static'))
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')