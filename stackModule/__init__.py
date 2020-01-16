#Details
VERSION = (0, 1)
__version__ = '.'.join(map(str, VERSION[0:2]))
__description__ = 'Stack module example in python'
__author__ = 'Brendan Jennings'
__author_email__ = 'jbrendan70@outlook.com'
__homepage__ = 'https://github.com/dudeisbrendan03/stack-example'
__license__ = 'BSD'
name = "stack-module"

#Classes
from .core import stackTools
