
try:
    print("Trying import local settings...")
    from to_do.config.local import *
except ImportError:
    print("Cant find local.  Trying coderannie.")
    from to_do.config.deploy import *
