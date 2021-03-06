"""
Common utility functions/classes for executable PY scripts.
"""

from functools import wraps
from pathlib import Path
import os
import traceback




ROOTPARENTDIR = Path(__file__).parent.parent.parent  #: "`pathlib.Path` to parent of root directory of PyYAUL."

def init():
	"""
	Doesn't do anything right now, but eventually will house essential functions like initializing
	the debug logging system.
	"""
	pass

class showError:
	"""
	Function decorator that will ensure the user sees any exception that occurred
	before execution leaves the function.  This is useful for situations such as
	the "main" method of an executable PY file in Windows, where the terminal
	would normally auto-close before the user had a chance to see the error
	message.
	"""
	def __init__(self, f):
		self.f = f
		wraps(f)(self)

	def __call__(self, *args, **kargs):
		try:
			ret = self.f(*args, **kargs)
		except:
			if os.name == 'nt':  #Windows will auto-close the terminal.
				print(
					'Exception encountered while attempting to execute {} with args '
					'({}, {}):'
					.format(repr(self.f), args, kargs),
				)
				traceback.print_exc()
				print('\nPress "Enter" to continue...\n')
				input()
			raise
		return ret
