#import imp
#import os
#import sys


#sys.path.insert(0, os.path.dirname(__file__))

#wsgi = imp.load_source('wsgi', 'accounter/wsgi.py')
#application = wsgi.callable





import os
import sys

path='/home/ytcvjcet/accounter'

if path not in sys.path:
  sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'accounter.settings'


import django.core.handlers.wsgi
import django

django.setup()
application = django.core.handlers.wsgi.WSGIHandler()


