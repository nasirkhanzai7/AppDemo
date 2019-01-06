# Production settings
from .production import *
try:
    # local settings
    from .local import *
except:
    pass
