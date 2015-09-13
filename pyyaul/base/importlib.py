"""
Utility functions for dealing with Python imports.
"""

import sys




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
    for syspath in sys.path:
        pathRel = path.relative_to(syspath)
        if pathRel.is_absolute():
            continue
        return ".".join(pathRel.parts).rsplit(".", 1)[0]
    else:
        raise ValueError('Given file "{}" is not within the Python\'s "sys.path" scope.')
