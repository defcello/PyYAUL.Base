# PyYAUL
Yet Another Utility Library.  A collection of utility functions/modules for
Python.

PyYAUL is designed to be split into component libraries that can be used
independently or together.  All component libraries will start with the root
import "pyyaul".

This is the "Base" component.  It requires only vanilla Python for all its modules.

====================================================================================================

I hate modification terror.  If there's a better way to do something, it's going to be implemented
even if it means voiding backwards compatibility.  We will do our best to add breadcrumbs for at
least a few revisions pointing you to the new way of doing things.  UPGRADE AT YOUR OWN RISK!

THIS CODE COMES WITH NO GUARANTEES.  THE DEVELOPERS ARE NOT RESPONSIBLE FOR ANY PROBLEMS USE OF THIS
LIBRARY MAY CAUSE.

## License
MIT (https://opensource.org/licenses/MIT)

## Status
A few modules for unit testing and basic program operation.  Mostly, I'm still focused on framework
development.

## Installation
### This project requires:
 - Python 3.8 or greater.

### Optional:
 - Sphinx for generating API documentation
   - Examples: "https://pythonhosted.org/an_example_pypi_project/sphinx.html"

## Usage

### To install:
There are options, but here's what I typically do:

1. `cd myproject/`
2. `mkdir lib`
3. `cd lib`
4. `git clone https://github.com/defcello/PyYAUL.Base pyyaulbase`
6. Somewhere in your code:
    ```python
        import pathlib
        import sys
        sys.path.append(str((pathlib.Path(__file__).parent / 'lib' / 'pyyaulbase').resolve()))
    ```

Ultimately, get the root folders of ["PyYAUL.Base"](https://github.com/defcello/PyYAUL.Base) in Python's `sys.path`.
