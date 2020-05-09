#! /usr/bin/env python3.7

"""
TXT file module.
"""

from pyyaul.base.file._base import File



class TxtFile(File):
	"""
	Class for representing a TXT file.
	"""

	data = None  #`str` representing the internal data of the file.

	def __init__(self, path=None):
		self.data = ''
		super().__init__(path)

	def _load(self, path):
		with path.open() as fd:
			self.data = fd.read()

	def _save(self, path):
		with path.open('w') as fd:
			fd.write(self.data)
