#! /usr/bin/env python3.7

"""
Base class for representing a file.
"""

from pyyaul.base.pathlib import Path
import os




class File:
	"""
	Base class for representing a file.
	"""

	path = None  #`pyyaul.base.pathlib.Path` object, or `None` if not representing a file in the file system.
	data = None  #`object` representing the internal data of the file.

	def __init__(self, path=None, load=True, createIfMissing=True):
		self._mtime = None
		if path is not None:
			self.path = self._pathResolve(path)
			if createIfMissing and not self.exists():
				self.save(path)
			elif load:
				self.load(path)

	def exists(self):
		if self.path is None:
			return False
		return self.path.exists()

	def isDiffFromDisk(self):
		"""
		@return `bool` `True` if the file has been modified in the file system
			since the last time `self.load` or `self.save` was called; `False`
			if not, or if `self.path` is `None`.
		"""
		if self.path is None or os.path.getmtime(self.path) == self._mtime:
			return False
		return True

	def load(self, path=None, *args, **kargs):
		"""
		@return Whatever is returned by `self._load`.
		"""
		path = self._pathResolve(path)
		ret = self._load(path, *args, **kargs)
		self.path = path
		self._mTimeUpdate()
		return ret

	def _load(self, path):
		"""
		Internal implementation of `load`.  Subclasses should override this with
		their own implementations as appropriate for the file type.
		@param path `pyyaul.base.pathlib.Path` object.  Guaranteed to not be
			`None`, but NOT guaranteed to be valid.
		"""
		pass

	def _pathResolve(self, path):
		if path is None:
			path = self.path
		if path is None:
			raise ValueError('Unable to resolve `path`.')
		if not isinstance(path, Path):
			path = Path(path)
		return path

	def save(self, path=None, *args, **kargs):
		"""
		@return Whatever is returned by `self._save`.
		"""
		path = self._pathResolve(path)
		ret = self._save(path, *args, **kargs)
		self.path = path
		self._mTimeUpdate()
		return ret

	def _save(self, path):
		"""
		Internal implementation of `save`.  Subclasses should override this with
		their own implementations as appropriate for the file type.
		@param path `pyyaul.base.pathlib.Path` object.  Guaranteed to not be
			`None`, but NOT guaranteed to be valid.
		"""
		pass

	def _mTimeUpdate(self):
		"""
		Updates `self._mtime` with the modification time currently in the file
		system.
		"""
		if self.path is None or not self.path.exists():
			return
		self._mtime = os.path.getmtime(self.path)
