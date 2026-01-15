"""
Version management system.
"""

class Version:

    clsPrev = None  #`Version` class that represents the previous version of `self`, or `None` if there is no previous `Version`.

    def __init__(self):
        pass

    def _initialize(self, obj):
        """
        Initializes `obj` to match this version from scratch.  `obj` may be
        modified in place, but regardless will be returned.

        By default, this will invoke `clsPrev._initialize` and use `self.update`
        to bring it to this version.  However, subclasses may override this to
        initialize to a later version.
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
        v = self.version(obj)
        if v is self.__class__:  #No update necessary.
            pass
        elif v is None:  #Build from scratch.
            obj = self._initialize(obj)
        elif clsPrev is not None:
            obj = self.clsPrev().update(obj)
            obj = self._update(obj)
        assert self.matches(obj)
        return obj  #Object

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
