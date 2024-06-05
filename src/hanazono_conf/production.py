import os

from .settings import *  # noqa

# Production settings
SECRET_KEY = os.environ.get("SECRET_KEY")
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS").split(",")
CSRF_TRUSTED_ORIGINS = ["https://" + host for host in ALLOWED_HOSTS]
DEBUG = False

# WhiteNoise configuration
MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")
STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"

# Redis Cache
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": f"redis://{os.environ.get("REDIS_HOST")}:{os.environ.get("REDIS_PORT")}",
    }
}

# Database
is_standalone = (
    os.environ.get("RENDER") is not None  # Render
    or os.environ.get("WEBSITE_INSTANCE_ID") is not None  # Azure
    or str(os.environ.get("STANDALONE", False)).lower() != "false"  # Set manually
)
if is_standalone:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": "sqlitedb",
        }
    }
