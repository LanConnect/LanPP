import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from django.core.management import setup_environ
import settings
setup_environ(settings)

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

