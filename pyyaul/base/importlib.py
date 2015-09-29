"""
Utility functions for dealing with Python imports.
"""

from math import inf
from pathlib import Path
import sys




def addToSysPath(*paths):
    """
    Adds the given path(s) to Python's `sys.path`.
    :param paths: Any number of `pathlib.Path` or `str` paths to add to
        `sys.path`.
    """
    for path in paths:
        if not isinstance(path, Path):
            path = Path(path)
        pathStr = str(path.resolve())
        if pathStr not in sys.path:
            sys.path.append(pathStr)

def fileImportPath(path):
    """
    Returns a string of the dotted path to the given module file.
    :param path: ``pathlib.Path`` object pointing to the module file you want to
        look up.
    :return: String.
    :throws ValueError: If given path is not importable from the current Python
        environment or path doesn't point to a PY, PYC, PYD, PYO, or PYW file.
    """
    if path.suffix not in (".py", ".pyc", ".pyd", ".pyo", ".pyw"):
        raise ValueError('Given file "{}" is not a Python module.'.format(path))
    ret = None
    retLen = inf
    #Protect against double imports by finding the shortest import path.
    for syspath in sys.path:
        try:
            pathRel = path.relative_to(syspath)
        except ValueError:
            continue
        if pathRel.is_absolute():
            continue
        pathImp = ".".join(pathRel.parts).rsplit(".", 1)[0]
        pathImpLen = len(pathImp)
        if pathImpLen < retLen:
            ret = pathImp
            retLen = pathImpLen
    if ret is None:
        raise ValueError('Given file "{}" is not within the Python\'s "sys.path" scope.')
    return ret
