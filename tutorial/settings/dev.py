from tutorial.settings.base import *

# Overide the base.py setting here

try:
	from tutorials.settings.local import *
except:
	pass