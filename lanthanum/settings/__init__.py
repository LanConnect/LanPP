import platform
import os, platform

if 'EPIO' in os.environ.keys():
    from epio import *
else:
    from base import *

#try to grab host specific configs
try:
    exec 'from %s import *' % (platform.node().split(".")[0].lower())
except ImportError:
    pass
except SyntaxError:
	pass

if SERVER_CLASS.lower() == "dev" or SERVER_CLASS.lower() == "test":
	DEBUG=True
elif SERVER_CLASS.lower() == "prd":
	DEBUG=False
