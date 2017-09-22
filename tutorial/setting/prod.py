from tutorial.setting import *

# Overide the base.py setting here

BASE_DIR = os.path.dirname(
	os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)


ALLOWED_HOSTS = ['*']

DEBUG = False

try:
	from tutorial.settings.local import *
except:
	pass


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}