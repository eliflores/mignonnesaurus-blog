import os

TEST_BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'test_key'
INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'blog',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(TEST_BASE_DIR, 'test_db.sqlite3'),
    }
}
