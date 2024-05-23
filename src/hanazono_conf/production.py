import os

from .settings import *  # noqa

# Production settings
SECRET_KEY = os.environ.get("SECRET_KEY")
ALLOWED_HOSTS = ["localhost", "127.0.0.1", os.environ.get("IP_ADDRESS")]
CSRF_TRUSTED_ORIGINS = ["http://" + host for host in ALLOWED_HOSTS]
DEBUG = False

# WhiteNoise configuration
MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")
STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"

# Redis Cache
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": f"redis://redis:{os.environ.get("REDIS_PORT")}",
    }
}
