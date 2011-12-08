import platform
import os, platform

if 'EPIO' in os.environ.keys():
    from epio import *
else:
    from base import *

#try to grab host specific configs
try:
    host_settings = __import__(platform.node().split(".")[0].lower())
    locals().update(host_settings.__dict__)
except ImportError:
    pass