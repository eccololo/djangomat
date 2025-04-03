from pathlib import Path
from decouple import config
from django.contrib.messages import constants as messages
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/


SECRET_KEY = config("SECRET_KEY")
DEBUG = config("DEBUG", default=False, cast=bool)


ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'jazzmin', # For Jazzmin Admin Panel Template
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # User apps
    'dataentry',
    'uploads',
    'emails',
    'image_compression',
    'stock_analysis',

    # Installed apps
    'crispy_forms',
    'crispy_bootstrap5',
    'ckeditor',
    "anymail",
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

ROOT_URLCONF = 'djangomat.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ["templates"],
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

WSGI_APPLICATION = 'djangomat.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'
STATICFILES_DIRS = [
    BASE_DIR / "djangomat/static",
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Media files configuration
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Messages framework
MESSAGE_TAGS = {
    messages.ERROR: "danger",
    messages.SUCCESS: "success"
}

# Celery Configuration
CELERY_BROKER_URL = 'redis://localhost:6380'

# Gmail Email Configuration
# EMAIL_HOST = config("EMAIL_HOST")
# EMAIL_PORT = config("EMAIL_PORT", cast=int)
# EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD")
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = config("EMAIL_HOST_USER")
# DEFAULT_FROM_EMAIL = f"Mateusz Hyla - Djangomat.com <{EMAIL_HOST_USER}>" # Email Default SUbject
# DEFAULT_TO_EMAIL = config("DEFAULT_TO_EMAIL")


# Brevo Email Configuration
EMAIL_BACKEND = "anymail.backends.sendinblue.EmailBackend"
ANYMAIL = {
    "SENDINBLUE_API_KEY": config("SENDINBLUE_API_KEY"),
}
EMAIL_HOST_USER = config("EMAIL_HOST_USER")
DEFAULT_FROM_EMAIL = f"Mateusz Hyla - Djangomat.com <{EMAIL_HOST_USER}>" # Email Default SUbject
DEFAULT_TO_EMAIL = config("DEFAULT_TO_EMAIL")

# Crispy forms settings
CRISPY_TEMPLATE_PACK = 'bootstrap5'

# CKEdityor Settings
CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'moono-lisa',  
        'contentsCss': '/static/css/ckeditor_dark.css',  
        'width': 'auto',       
        'height': 300, 
    },
}

# TODO: Here you must change in settings.py BASE_URL on URL of your website. If you are using ngrok change BASE URL on ngrok URL in settings.py.
# NGROK SETTINGS
BASE_URL = "<ngrok-url>"
# CSRF_TRUSTED_ORIGINS = ["<ngrok-url>"]