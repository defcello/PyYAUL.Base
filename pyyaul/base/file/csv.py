#! /usr/bin/env python3.7

"""
CSV file module.
"""

from pyyaul.base.file._base import File
import csv



class CsvFile(File):
	"""
	Class for representing a JSON file.
	"""

	data = None  #`list` of `list`s representing the internal data of the file.

	def __init__(self, path=None):
		self.data = []
		super().__init__(path)

	def _load(self, path):
		try:
			with path.open('r') as fd:
				reader = csv.reader(fd, 'excel')
				self.data = list(r for r in reader)
		except FileNotFoundError:
			self.data = []

	def _save(self, path):
		with path.open('w') as fd:
			writer = csv.writer(fd, 'excel')
			for r in self.data:
				writer.writerow(r)
