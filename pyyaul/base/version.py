"""
Version management system.
"""

class Version:

    clsPrev = None  #`Version` class that represents the previous version of `self`, or `None` if there is no previous `Version`.
    schema_version = None

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        clsPrev = getattr(cls, 'clsPrev', None)
        explicit_schema_version = cls.__dict__.get('schema_version', None)
        if clsPrev is None:
            auto_schema_version = 0
        else:
            auto_schema_version = clsPrev.schema_version + 1
        if explicit_schema_version is None:
            cls.schema_version = auto_schema_version
        elif clsPrev is not None and explicit_schema_version <= clsPrev.schema_version:
            raise ValueError(
                '`schema_version` must be greater than the previous version '
                f'({explicit_schema_version=} <= {clsPrev.schema_version=}).'
            )

    def __init__(self):
        pass

    def _initialize(self, obj) ->object:
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

    def matches(self, obj :object) ->bool:
        """
        Returns `True` if `obj` matches this `Version`.
        """
        return False

    def update(self, obj :object) ->object:
        """
        Updates `obj` from a previous `Version` to this `Version`.  `obj` may be
        modified in place, but regardless will be returned.
        """
        v = self.version(obj)
        if v is self.__class__:  #No update necessary.
            pass
        elif v is None:  #Build from scratch.
            obj = self._initialize(obj)
        elif self.clsPrev is not None:
            obj = self.clsPrev().update(obj)
            obj = self._update(obj)
        assert self.matches(obj)
        return obj  #Object

    def _update(self, obj :object) ->object:
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

    @classmethod
    def version_class_from_schema_version(cls, schema_version):
        """
        Returns the `Version` subclass that owns `schema_version`, or `None` if
        there is no matching class in this version chain.
        """
        if cls.schema_version == schema_version:
            return cls
        if cls.clsPrev is None:
            return None
        return cls.clsPrev.version_class_from_schema_version(schema_version)
