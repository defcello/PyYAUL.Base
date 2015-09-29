"""
`__init__.py` files are demons.  This little demon is here to make sure users
don't import this library the wrong way, risking double-import issues.
"""

from pathlib import Path




raise Exception(
  'Unsupported import path for PyYAUL.  Please add "{}" to your `sys.path` '
  'and import using `from defcello import ...`.'
  .format(Path(__file__).parent),
)
