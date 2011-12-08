# Django settings for AvconTournaments project.
import sys, pinax
from os.path import abspath, join, dirname

PROJECT_ROOT = abspath(dirname(__file__)); sys.path.append(PROJECT_ROOT)
PINAX_ROOT = abspath(dirname(pinax.__file__))
LC_ROOT = (join(PROJECT_ROOT, '..', '..', 'Lan 2.0', 'LanConnect'); sys.path.append(LC_ROOT)


SITE_NAME = 'Lan++'

DEBUG = True
TEMPLATE_DEBUG = DEBUG
SERVE_MEDIA = DEBUG

ADMINS = (
	# ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',  # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
		'NAME': 'dev.db3',                       # Or path to database file if using sqlite3.
		'USER': '',                              # Not used with sqlite3.
		'PASSWORD': '',                          # Not used with sqlite3.
		'HOST': '',                              # Set to empty string for localhost. Not used with sqlite3.
		'PORT': '',                              # Set to empty string for default. Not used with sqlite3.
	}
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Australia/Adelaide'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-au'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = join(ROOT_PATH,'media')
MEDIA_URL = '/media/'

STATIC_ROOT = join(ROOT_PATH, 'static-root')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
	join(ROOT_PATH,'static'),
	join(PINAX_ROOT, "media", PINAX_THEME),
)

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = STATIC_URL+'admin/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'd6%#o+0dae7*h+7&8gt6469kzh*fglpv4q-i$te-ew=hz(y%1&'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
	'django.template.loaders.filesystem.Loader',
	'django.template.loaders.app_directories.Loader',
	#'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
	#'debug_toolbar.middleware.DebugToolbarMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
	'debug_toolbar.middleware.DebugToolbarMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
	# default template context processors
	'django.core.context_processors.auth',
	'django.core.context_processors.debug',
	'django.core.context_processors.i18n',
	'django.core.context_processors.media',
	'django.core.context_processors.static',
	'django.core.context_processors.request',
	'django.contrib.messages.context_processors.messages',

	'lanthanum.context_processors.settings',
	'lanthanum.context_processors.versions',

	"pinax.core.context_processors.pinax_settings",
	"pinax.apps.account.context_processors.account",

	"notification.context_processors.notification",
	"announcements.context_processors.site_wide_announcements",
	"messages.context_processors.inbox",
	"friends_app.context_processors.invitations",

	"lanthanum.context_processors.combined_inbox_count",
)

TEMPLATE_DIRS = (
	# Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
	# Always use forward slashes, even on Windows.
	# Don't forget to use absolute paths, not relative paths.
	join(ROOT_PATH,'templates'),
	join(PINAX_ROOT, 'templates', PINAX_THEME),
)

INSTALLED_APPS = (
	#'admin_tools',
	#'admin_tools.theming',
	#'admin_tools.menu',
	#'admin_tools.dashboard',
	
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.sites',
	'django.contrib.messages',
	'django.contrib.admin',
	'django.contrib.staticfiles',
	'django.contrib.flatpages',
	
	'sorl.thumbnail',
	'debug_toolbar',
	'south',
	'markitup',
	
	#'paging',
	#'sentry',
	#'sentry.client',
	# Uncomment the next line to enable admin documentation:
	# 'django.contrib.admindocs',
	
	#'LanConnect.jquery',
	#'LanConnect.joust',
)

#match any server on home network.
if DEBUG:
	from fnmatch import fnmatch
	class glob_list(list):
		def __contains__(self, key):
			for elt in self:
				if fnmatch(key, elt): return True
			return False
	INTERNAL_IPS = glob_list(['127.0.0.1', '192.168.*', '172.24.*'])

ROOT_URLCONF = 'urls'

SENTRY_KEY = 'magic8balls'

JOUST_SMS_NOTIFICATIONS = True

INTERNAL_IPS = ('127.0.0.1',)
if 'debug_toolbar' in INSTALLED_APPS:
    DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS': False,
    }

if 'markitup' in INSTALLED_APPS:
    MARKITUP_FILTER = ('markdown.markdown', {
                            'safe_mode': True,
                        })

