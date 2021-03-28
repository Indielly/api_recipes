from application.settings import BASE_DIR, ROOT_URLCONF, STATIC_ROOT, INSTALLED_APPS
from django.core.management.utils import get_random_secret_key

SECRET_KEY = get_random_secret_key()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'tests/test_db.sqlite3',
    }
}