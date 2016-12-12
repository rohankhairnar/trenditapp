"""
Django settings for trenditapp project.

Generated by 'django-admin startproject' using Django 1.10.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_e^&e!6ugms=%_(t0f-f&@%&#7#r&o6@u+@4dxse%mb-wadh6^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mainapp',
    'django_forum',
    'twitterapp',
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

ROOT_URLCONF = 'trenditapp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'trenditapp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'EST'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_ROOT = '/static/'
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "templates/static"), ]
LOGIN_URL = '/mainapp/login/'

#For sending email settings:
EMAIL_HOST = 'smtp.googlemail.com'
EMAIL_PORT = 587
EMAIL_HOST_PASSWORD = '' #add your gmail password here
EMAIL_HOST_USER = '<idname>@gmail.com'  #add your gmail ID here
EMAIL_USE_TLS   = True

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

TWITTER_FEED_CONSUMER_PUBLIC_KEY = 'k7TcWQNvLAFw6UHp8b6tjSfys'
TWITTER_FEED_CONSUMER_SECRET = 'HoJ4C5Qgb0kGpt1NkPp4RAuInseNYOHLXOXrpksAU7jwRdW2ZY'
TWITTER_FEED_OPEN_AUTH_TOKEN = '105425189-p1Oif8hdJ4RXuN35mbPfH81onaVScOaziCefbRxJ'
TWITTER_FEED_OPEN_AUTH_SECRET = '8gikBBD7lRt7mbGG9JO5Yfy9kMS4OjesrN0UQIZaOEJOI'


from django.conf import settings

DJANGO_SIMPLE_FORUM_TOPICS_PER_PAGE = getattr(settings, 'DJANGO_SIMPLE_FORUM_TOPICS_PER_PAGE', 10)
DJANGO_SIMPLE_FORUM_REPLIES_PER_PAGE = getattr(settings, 'DJANGO_SIMPLE_FORUM_REPLIES_PER_PAGE', 10)
DJANGO_SIMPLE_FORUM_FILTER_PROFANE_WORDS = getattr(settings, 'DJANGO_SIMPLE_FORUM_FILTER_PROFANE_WORDS', True)

