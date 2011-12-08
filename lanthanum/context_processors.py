""" Useful Context Processors """

from django.conf import settings as django_settings
from sys import modules
from argparse import ArgumentError

def settings(request=None):
    return {'settings': django_settings }

class VersionFinder():
    def __getattr__(self, name):
        if not name.startswith("_"):
            try:
                app = __import__(name)
                try: return app.get_version()
                except: pass
                try: return ".".join(app.VERSION)
                except: pass
                try: return ".".join(app.__version__)
                except: pass
                
            except ImportError:
                pass
        raise ArgumentError

def versions(request=None):
    return {'versions': VersionFinder()}