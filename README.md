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
 - Python 3.4 or greater (requires implicit namespace packages and "pathlib" CAUSE THEY'RE AWESOME)

### Optional:
 - Sphinx for generating API documentation
   - Examples: "https://pythonhosted.org/an_example_pypi_project/sphinx.html"

## Usage

### To install:
I typically use PyYAUL as a Git submodule in my projects (for easy version
tracking) and add its root folder to the `sys.path` (hence the defensive
"__init__.py"), but you can use Git subtree (especially if you want a small
subset of the modules), toss it in your Python site-packages folder using the
"setup.py" that'll inevitably get added, or clone it and add its root folder to
your project's `sys.path`.

### To run:
https://www.youtube.com/watch?v=8XiwtiDTlYU
