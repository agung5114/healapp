# import importlib as imp
# import os
# import sys


# sys.path.insert(0, os.path.dirname(__file__))

# wsgi = imp.load_source('wsgi', 'passenger_wsgi.py')
# # application = wsgi.application

from core.wsgi import application
# application = application

# import sys

# sys.path.insert(0, "/home/gaspolte/dashapp/gtech")

# import os
# os.environ['DJANGO_SETTINGS_MODULE'] = 'gtech.settings'

# from django.core.wsgi import get_wsgi_application
# application = get_wsgi_application()