from .base import *
import os
import subprocess
import os

# Trouver GDAL automatiquement sur Linux
try:
    gdal_path = subprocess.check_output(['gdal-config', '--prefix']).decode().strip()
    GDAL_LIBRARY_PATH = f"{gdal_path}/lib/libgdal.so"
    GEOS_LIBRARY_PATH = "/usr/lib/libgeos_c.so"
except Exception:
    pass



DEBUG = False

ALLOWED_HOSTS = ['*']

# Base de données PostgreSQL Railway
DATABASES = {
    "default": {
        "ENGINE": "django.contrib.gis.db.backends.postgis",
        "NAME": os.environ.get("PGDATABASE", "railway"),
        "USER": os.environ.get("PGUSER", "postgres"),
        "PASSWORD": os.environ.get("PGPASSWORD"),
        "HOST": "thomas.proxy.rlwy.net",
        "PORT": "35213",
    }
}
# Sécurité
SECRET_KEY = os.environ.get("SECRET_KEY", "change-me-in-production")

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = "DENY"

# Email
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = os.environ.get("EMAIL_HOST", "smtp.gmail.com")
EMAIL_PORT = int(os.environ.get("EMAIL_PORT", 587))
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER", "")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD", "")
DEFAULT_FROM_EMAIL = os.environ.get("DEFAULT_FROM_EMAIL", "")

# Static files
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "django.contrib.staticfiles.storage.StaticFilesStorage"

# CORS
CORS_ALLOW_ALL_ORIGINS = True

# Redis / Celery
CELERY_BROKER_URL = os.environ.get("REDIS_URL", "redis://localhost:6379/0")
CELERY_RESULT_BACKEND = os.environ.get("REDIS_URL", "redis://localhost:6379/1")

# Logging
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "INFO",
    },
}