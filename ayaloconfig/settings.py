"""
Django settings for ayaloconfig project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import dj_database_url
import os
from decouple import config, Csv
import dj_database_url
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-#5bt^n*!l_w!dcncb3a!+n69v1q1h2wf@rou$d)x&p4!ygo_e)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    "authemail",
    "ayaloapp",
    "productlisting_api",
    'drf_yasg',    
    'order_api',
    'corsheaders'


]

MEDIA_URL='/media/'
MEDIA_ROOT=os.path.join(BASE_DIR, 'media')

# PHONE_VERIFICATION = {
#     "BACKEND": "phone_verify.backends.twilio.TwilioBackend",
#     "OPTIONS": {
#         "SID": "fake",
#         "SECRET": "fake",
#         "FROM": "+14755292729",
#         "SANDBOX_TOKEN": "123456",
#     },
#     "TOKEN_LENGTH": 6,
#     "MESSAGE": "Welcome to {app}! Please use security code {security_code} to proceed.",
#     "APP_NAME": "Phone Verify",
#     "SECURITY_CODE_EXPIRATION_TIME": 3600,  # In seconds only
#     "VERIFY_SECURITY_CODE_ONLY_ONCE": False,  # If False, then a security code can be used multiple times for verification

REST_FRAMEWORK = {
	'DEFAULT_AUTHENTICATION_CLASSES': (
		'rest_framework.authentication.TokenAuthentication',
	)
}
TEMPLATE_DIR=os.path.join(BASE_DIR, "templates")

CORS_ALLOW_ALL_ORIGINS=True

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware'
]

ROOT_URLCONF = 'ayaloconfig.urls'

TEMPLATE_DIR=os.path.join(BASE_DIR, "templates")

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
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


WSGI_APPLICATION = 'ayaloconfig.wsgi.application'

SWAGGER_SETTINGS={
    'JSON_EDITOR': True
}

DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')

)

}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

FIXTURE_DIRS = (
   os.path.join(BASE_DIR, 'fixtures'),
)



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT=os.path.join(BASE_DIR,'staticfiles')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'ayaloapp.MyUser'

EMAIL_FROM = "Ayalo-Online"
# EMAIL_BCC=config('EMAIL_ADDRESS')

EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = config('HOST_USER')
EMAIL_HOST_PASSWORD = config('PASSWORD')
EMAIL_USE_TLS = True


STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'
# SID = config('Account_sid')
# SECRET = config('Auth_token')
# FROM = config('Phone_number')
