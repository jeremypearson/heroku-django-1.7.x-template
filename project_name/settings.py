"""
Django settings for {{ project_name }} project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

def getBool(myString):
    return True if myString.lower() == "true" else False

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

def printAllEnvironVars():
    print "Environment variables:"
    for index, each in enumerate(sorted(os.environ.iteritems())):
        print index, each

#printAllEnvironVars()


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = getBool(os.environ['DEBUG'])

TEMPLATE_DEBUG = getBool(os.environ['TEMPLATE_DEBUG'])

# Display state of DEBUG mode
if DEBUG:
    print "DEBUG mode is on."
else:
    print "DEBUG mode is off."

# Display state of TEMPLATE_DEBUG mode
if TEMPLATE_DEBUG:
    print "TEMPLATE_DEBUG mode is on."
else:
    print "TEMPLATE_DEBUG mode is off."

# Hosts
ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myApp',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = '{{ project_name }}.urls'

WSGI_APPLICATION = '{{ project_name }}.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {}
if os.environ['DATABASE_URL'] == 'sqlite' or os.environ['DATABASE_URL'] == 'sqlite://':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
else:
    import dj_database_url
    DATABASES['default'] = dj_database_url.config()

print "default database's ENGINE:", str(DATABASES['default']['ENGINE'])
print "default database's NAME:", str(DATABASES['default']['NAME'])

# Honor the 'X-Forewarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
