"""
Version management system.
"""

class Version:

	clsPrev = None  #`Version` class that represents the previous version of `self`, or `None` if there is no previous `Version`.

	def __init__(self):
		pass

	def _initialize(self, obj=None):
		"""
		Initializes `obj` to match this version from scratch.  `obj` may be
		modified in place, but regardless will be returned.

		May be overridden by subclasses.
		"""
		if self.clsPrev is None:
			raise NotImplementedError()
		obj = self.clsPrev()._initialize(obj)
		return self.update(obj)

	def matches(self, obj):
		"""
		Returns `True` if `obj` matches this `Version`.
		"""
		return False

	def update(self, obj):
		"""
		Updates `obj` from a previous `Version` to this `Version`.  `obj` may be
		modified in place, but regardless will be returned.
		"""
		if not self.matches(obj):
			if self.clsPrev is None:
				obj = self._initialize(obj)
			else:
				obj = self.clsPrev().update(obj)
		return self._update(obj)

	def _update(self, obj):
		"""
		Internal implementation to be overridden by subclasses.  Only gets
		called once `obj` is the same version as `self._prev`.  `obj` may be
		modified in place, but regardless should be returned.
		"""
		raise NotImplementedError()

	def version(self, obj):
		"""
		Returns the `Version` matching `obj`, or `None` if no match was found.
		"""
		if self.matches(obj):
			return self.__class__
		if self.clsPrev is None:
			return None
		return self.clsPrev().version(obj)
