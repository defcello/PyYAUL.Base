#! /usr/bin/env python3.7

"""
Expansion of Python's `pathlib`.
"""

import os
import pathlib




class Path(pathlib.Path):

	__slots__ = ()

	def __eq__(self, rhs):
		"""
		Will now allow comparing to `str`s.
		"""
		if isinstance(rhs, str):
			rhs = Path(rhs)
		return super().__eq__(rhs)

	def is_subdir(self, *others):
		"""
		Determines if this `Path` is in the given path.  For example:
			>>> Path("/usr/bin/python3").is_subdir("/usr")
			True
			>>> Path("/usr/bin/python3").is_subdir("/usr/bin")
			True
			>>> Path("/usr/bin/python3").is_subdir("/usr/bin/python3")
			False
			>>> Path("/usr/bin").is_subdir("/usr/bin/python3")
			False
		"""
		try:
			p = super().relative_to(*others)
		except ValueError:
			return False
		return p != "."

	def is_supdir(self, *others):
		"""
		Determines if the given path is within this `Path`.  For example:
			>>> Path("/usr").is_superdir("/usr/bin/python3")
			True
			>>> Path("/usr/bin").is_superdir("/usr/bin/python3")
			True
			>>> Path("/usr/bin/python3").is_superdir("/usr/bin/python3")
			False
			>>> Path("/usr/bin/python3").is_superdir("/usr/bin")
			False
		"""
		return Path(*others).is_subdir(self)
		
	def __len__(self):
		"""Returns the `int` number of parts in the path."""
		return len(self.parts)

	def __new__(cls, *args, **kargs):
		#...because the dev forgot to support subclasses.
		cls = WindowsPath if os.name == 'nt' else PosixPath
		return pathlib.Path.__new__(cls, *args, **kargs)

	def relative_to(self, *others):
		"""
		Customized form that, rather than throwing a ValueError if the given
		path is not a parent directory, will simply return the relative form,
		including ".." elements if necessary and an absolute path if no relative
		path is available.
		"""
		#Move this behavior closer to `os.path.relpath`.
		try:
			return super().relative_to(*others)
		except ValueError:
			p = Path(*others)
			return Path(os.path.relpath(str(self), str(p)))

class PosixPath(Path, pathlib.PosixPath):
	__slots__ = ()

class WindowsPath(Path, pathlib.WindowsPath):
	__slots__ = ()
