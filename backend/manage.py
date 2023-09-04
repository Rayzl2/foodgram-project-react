import os
import sys


def Startup():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings")
    
    try:
        
        from django.core.management import execute_from_command_line
    
    except ImportError as exc:
        
        raise ImportError("Import Error. May be libraries or env init error") from exc 
        execute_from_command_line(sys.argv)



Startup()
