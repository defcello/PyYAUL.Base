"""
Utility module for unit testing in Python.
"""

from pathlib import Path
from pyyaul.base.importlib import fileImportPath
import os
import sys
import unittest




def runTestsIn(path):
	"""
	Runs all unit tests found in the given path and it subdirectories.  To qualify
	as a unit test module, a file must match the following criteria:
	* Lie within a "_test" directory.
	* Match the file name pattern "test*.py".
	An example unit test filename would be
	"/path/to/project/_test/test_mymodule.py".  Test results are printed to
	STDOUT.

	:param path: ``pathlib.Path`` object pointed to the root directory that tests
	should be discovered in and run from.
	:rtype: ``unittest.TestResult``
	"""
	loader = unittest.defaultTestLoader
	tests = unittest.TestSuite()
	print(f'Searching for tests in {path!r}...')
	for testDir in path.glob('**/_test'):
		print(f'Searching {testDir!r}...')
		#Cause Python's "discover" method fails on implicit namespace packages...
		for testFile in testDir.glob('**/test*.py'):
			moduleName = fileImportPath(testFile)
			tests.addTest(loader.loadTestsFromName(moduleName))
	return unittest.TextTestRunner().run(tests)
