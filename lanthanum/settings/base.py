# Django settings for AvconTournaments project.
import sys
from os.path import abspath, join, dirname

PROJECT_ROOT = join(abspath(dirname(__file__)),'..'); sys.path.append(PROJECT_ROOT)

SITE_NAME = 'Lan++'

DEBUG = True
TEMPLATE_DEBUG = DEBUG
SERVE_MEDIA = DEBUG

ADMINS = (
	# ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

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

TIME_ZONE = 'Australia/Adelaide'

SITE_ID = 1

LANGUAGE_CODE = 'en-au'
USE_I18N = True
USE_L10N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = join(PROJECT_ROOT,'media')
MEDIA_URL = '/media/'

STATIC_ROOT = join(PROJECT_ROOT, 'static-root')
STATIC_URL = '/static/'
STATICFILES_DIRS = ( join(PROJECT_ROOT,'static'), )

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = STATIC_URL+'admin/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'd6%#o+0dae7*h+7&8gt6469kzh*fglpv4q-i$te-ew=hz(y%1&'

ROOT_URLCONF = 'urls'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
	'django.template.loaders.filesystem.Loader',
	'django.template.loaders.app_directories.Loader',
	#'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
	'django.middleware.common.CommonMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
	'debug_toolbar.middleware.DebugToolbarMiddleware',
)


TEMPLATE_DIRS = ( join(PROJECT_ROOT,'templates'), )

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
)


#----- App Configuration ------
if 'LanConnect' in INSTALLED_APPS:
	LC_ROOT = join(PROJECT_ROOT, '..', '..', 'Lan 2.0', 'LanConnect'); sys.path.append(LC_ROOT)
	
	JOUST_SMS_NOTIFICATIONS = True

if 'pinax' in INSTALLED_APPS:
	import pinax; PINAX_ROOT = abspath(dirname(pinax.__file__))
	
	PINAX_THEME = "default"
	TEMPLATE_CONTEXT_PROCESSORS += (
		"pinax.core.context_processors.pinax_settings",
		"pinax.apps.account.context_processors.account",
	
		"notification.context_processors.notification",
		"announcements.context_processors.site_wide_announcements",
		"messages.context_processors.inbox",
		"friends_app.context_processors.invitations",
	
		"lanthanum.context_processors.combined_inbox_count",
	)
	TEMPLATE_DIRS += (join(PINAX_ROOT, 'templates', PINAX_THEME),)

if 'sentry' in INSTALLED_APPS:
	
	SENTRY_KEY = 'magic8balls'


INTERNAL_IPS = ('127.0.0.1',)
if 'debug_toolbar' in INSTALLED_APPS:
	DEBUG_TOOLBAR_CONFIG = {
		'INTERCEPT_REDIRECTS': False,
	}

if 'markitup' in INSTALLED_APPS:
	MARKITUP_FILTER = ('markdown.markdown', {
							'safe_mode': True,
						})

#match any server on home network.

if DEBUG:
	from fnmatch import fnmatch
	class glob_list(list):
		def __contains__(self, key):
			for elt in self:
				if fnmatch(key, elt): return True
			return False
	INTERNAL_IPS = glob_list(['127.0.0.1', '192.168.*', '172.24.*'])
