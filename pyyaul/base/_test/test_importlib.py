"""
Test module for `pyyaul.base.importlib`.
"""

import unittest
from unittest import TestCase
from pyyaul.base.execommon import ROOTPARENTDIR




class Test_fileImportPath(TestCase):

    def setUp(self):
        from pyyaul.base import importlib
        self.m = importlib

    def test_basic(self):
        act = self.m.fileImportPath(ROOTPARENTDIR / 'pyyaul' / 'base' / 'unittest.py')
        exp = 'pyyaul.base.unittest'
        self.assertEquals(act, exp)
