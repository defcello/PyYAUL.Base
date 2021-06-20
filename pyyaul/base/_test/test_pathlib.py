"""
Unit tests for `pyyaul.base.pathlib`.
"""

from pathlib import Path
from unittest import TestCase
import os
import sys

sys.path.append(Path(__file__).parent.parent.parent.parent)




class TestPath(TestCase):

	def setUp(self):
		from pyyaul.base import pathlib
		self.m = pathlib

	def testEqStr(self):
		self.assertEquals(self.m.Path("/"), "/")

	def testRelTo(self):
		if os.name == "nt":
			self.assertEquals(self.m.Path("C:/").relative_to("C:/Windows"), "..")
			self.assertEquals(self.m.Path("C:/").relative_to("C:/"), ".")
			self.assertEquals(self.m.Path("C:/Windows").relative_to("C:/"), "Windows")
		else:
			self.assertEquals(self.m.Path("/").relative_to("/usr"), "..")
			self.assertEquals(self.m.Path("/").relative_to("/"), ".")
			self.assertEquals(self.m.Path("/usr").relative_to("/"), "usr")
		#Can't think of a multiplatform way of testing impossible relative paths.

	def testIsSubDir(self):
		if os.name == "nt":
			self.assertTrue(self.m.Path("C:/Windows").is_subdir("C:/"))
			self.assertFalse(self.m.Path("C:/").is_subdir("C:/"))
			self.assertFalse(self.m.Path("C:/").is_subdir("C:/Windows"))
		else:
			self.assertTrue(self.m.Path("/usr").is_subdir("/"))
			self.assertFalse(self.m.Path("/").is_subdir("/"))
			self.assertFalse(self.m.Path("/").is_subdir("/usr"))

	def testIsSupDir(self):
		if os.name == "nt":
			self.assertTrue(self.m.Path("C:/").is_supdir("C:/Windows"))
			self.assertFalse(self.m.Path("C:/").is_supdir("C:/"))
			self.assertFalse(self.m.Path("C:/Windows").is_supdir("C:/"))
		else:
			self.assertTrue(self.m.Path("/").is_supdir("/usr"))
			self.assertFalse(self.m.Path("/").is_supdir("/"))
			self.assertFalse(self.m.Path("/usr").is_supdir("/"))
