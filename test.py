#! /usr/bin/env python3.8

from pathlib import Path
from pyyaul.base import unittest
import sys




if __name__ == '__main__':
	sys.path.append(str(Path(__file__).parent.resolve()))
	unittest.runTestsIn(Path(__file__).parent.resolve())
