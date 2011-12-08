from .base import *
from bundle_config import config #Epio provided config


MEDIA_ROOT = PROJECT_ROOT/'../data'
STATIC_ROOT = PROJECT_ROOT/'static-root'

#----- Haystack Config -----
HAYSTACK_SEARCH_ENGINE = 'solr'
HAYSTACK_SOLR_URL = "http://%(host)s:%(port)s%(path)s" % config['solr']
print "init'd solr on", HAYSTACK_SOLR_URL

#----- Reddis Session Backend -----
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'

#----- Django Internals -----
DATABASES['default'] = {
        'ENGINE':   'django.db.backends.postgresql_psycopg2',
        'NAME':     config['postgres']['database'],
        'USER':     config['postgres']['username'],
        'PASSWORD': config['postgres']['password'],
        'HOST':     config['postgres']['host'],
    }

CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': '%(host)s:%(port)s' % config['redis'],
        'OPTIONS': {
            'PASSWORD': config['redis']['password'],
        },
        'VERSION': config['core']['version'],
    },
}
