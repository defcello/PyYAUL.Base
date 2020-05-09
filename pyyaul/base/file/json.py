#! /usr/bin/env python3.7

"""
JSON file module.
"""

from pyyaul.base.file._base import File
import json



class JsonFile(File):
	"""
	Class for representing a JSON file.
	"""

	data = None  #`dict` (default) -OR- `list` representing the internal data of the file.

	def __init__(self, path=None):
		self.data = {}
		super().__init__(path)

	def get(self, keys, default=None, reload=False):
		"""
		Retrieves the value at the given key path, or `default` if no value was
		found.
		@param keys `str` or iterable of `str` objects indicating the key path
			to read from.
		@param default `object` to return in the event that the path indicated
			by `keys` does not exist.
		@param reload If `True`, will refresh the contents of the file from
			the file system before attempting to read from `self.data`.  Ignored
			if `self.path` is `None`.  Will overwrite any unsaved changes!
		@return `object` at the given `keys` path, or `default` if no value is
			defined.
		"""
		if reload and self.path is not None:
			self.load()
		if isinstance(keys, str):
			keys = (keys,)
		if self.data is None:
			return default
		fence = self.data.get(keys[0], {})
		for k in keys[1:-1]:
			fence = fence.get(k, {})
		return fence.get(keys[-1], default)

	def _load(self, path):
		try:
			with path.open('r') as fd:
				self.data = json.load(fd)
		except FileNotFoundError:
			self.data = {}

	def _save(self, path):
		with path.open('w') as fd:
			json.dump(self.data, fd, sort_keys=True, indent=4, separators=(',', ': '))

	def set(self, keys, val, save=False):
		"""
		@param keys `str` or iterable of `str` objects indicating the key path
			to write to.
		@param val Value to store.
		@param save If `True`, will save the changes to the file system.
			Ignored if `self.path` is `None`.
		@return `None`.
		"""
		if isinstance(keys, str):
			keys = (keys,)
		if self.data is None:
			data = {}
		data.setdefault(keys[0], {})
		fence = data[keys[0]]
		for k in keys[1:-1]:
			fence.setdefault(k, {})
			fence = fence[k]
		fence[keys[-1]] = val
		if save and self.path is not None:
			self.save()
