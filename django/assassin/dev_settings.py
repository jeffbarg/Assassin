#    ____             __                 ______        __ 
#   / __/_____ ______/ /____  ___ ___   /_  __/__ ____/ / 
#  / _// __/ // / __/ __/ _ \(_-</ -_)   / / / -_) __/ _ \
# /_/ /_/  \_,_/\__/\__/\___/___/\__/   /_/  \__/\__/_//_/


# Django settings for assassin project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
	# ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
		'NAME': 'HMX.sqlite',                      # Or path to database file if using sqlite3.
		# The following settings are not used with sqlite3:
		'USER': '',
		'PASSWORD': '',
		'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
		'PORT': '',                      # Set to empty string for default.
	}
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = '/Users/jeffbarg/Sites/assassin/THIS_DOES_NOT_EXIST/'

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
	'/Users/jeffbarg/Sites/assassin/static/',
	# Put strings here, like "/home/html/static" or "C:/www/django/static".
	# Always use forward slashes, even on Windows.
	# Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
	'django.contrib.staticfiles.finders.FileSystemFinder',
	'django.contrib.staticfiles.finders.AppDirectoriesFinder',
	# 'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'p(nv#q763t+-&cftr)xn9g9#5#cn0j9=jvej+q0_k6(&@kliyt'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
	'django.template.loaders.filesystem.Loader',
	'django.template.loaders.app_directories.Loader',
	# 'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages",

    "allauth.account.context_processors.account",
    "allauth.socialaccount.context_processors.socialaccount",
)

AUTHENTICATION_BACKENDS = (
    "allauth.account.auth_backends.AuthenticationBackend",
)

MIDDLEWARE_CLASSES = (
	'django.middleware.common.CommonMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	# Uncomment the next line for simple clickjacking protection:
	# 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'assassin.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'assassin.wsgi.application'

TEMPLATE_DIRS = (
	"/Users/jeffbarg/Sites/assassin/templates",
	# Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
	# Always use forward slashes, even on Windows.
	# Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.sites',
	'django.contrib.messages',
	'django.contrib.staticfiles',

	'django.contrib.admin',
	'django.contrib.admindocs',

	'games',
	'gameplay',	
	'main',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
	    'allauth.socialaccount.providers.facebook',

	'bootstrapform',

	'south',
)


# LOGIN_URL           = 'django.contrib.auth.views.login'
# LOGOUT_URL          = 'django.contrib.auth.views.logout'
# LOGIN_REDIRECT_URL  = 'games.views.index'

# AUTH_USER_MODEL = 'django_facebook.FacebookCustomUser'

# DJANGO_FACEBOOK https://github.com/tschellenbach/Django-facebook

FACEBOOK_APP_ID     = '465041326919886'
FACEBOOK_APP_SECRET = 'b6c9ac1913db9f36b591b59c5987221d'

SOCIALACCOUNT_PROVIDERS = \
    { 'facebook':
        { 'SCOPE': ['email'],
          'AUTH_PARAMS': { 'auth_type':  '' },
          'METHOD': 'oauth2' ,
          'LOCALE_FUNC': lambda request: 'en_US'} }

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_USERNAME_REQUIRED = False


# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
	'version': 1,
	'disable_existing_loggers': False,
	'filters': {
		'require_debug_false': {
			'()': 'django.utils.log.RequireDebugFalse'
		}
	},
	'handlers': {
		'mail_admins': {
			'level': 'ERROR',
			'filters': ['require_debug_false'],
			'class': 'django.utils.log.AdminEmailHandler'
		}
	},
	'loggers': {
		'django.request': {
			'handlers': ['mail_admins'],
			'level': 'ERROR',
			'propagate': True,
		},
	}
}

ALLOWED_HOSTS = (
	'127.0.0.1',
	'localhost',
)