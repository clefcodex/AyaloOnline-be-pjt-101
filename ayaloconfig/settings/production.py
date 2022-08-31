from .base import *
from decouple import config

CORS_ALLOW_ALL_ORIGINS=True

DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')

)
}

STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'