from to_do.config.base import *

# try:
#     print("Trying dev settings...")
#     from to_do.config.local import *
# except ImportError:
    print("Cant find local.  Trying deploy settings.")
    from to_do.config.deploy import *
