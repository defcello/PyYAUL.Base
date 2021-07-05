"""
Test module for `pyyaul.base.importlib`.
"""

import unittest
from unittest import TestCase
from pyyaul.base.execommon import ROOTPARENTDIR




class Test_Version(TestCase):

	def setUp(self):
		from pyyaul.base import version
		self.m = version
		class TestStringV0(version.Version):
			def _initialize(self, obj):
				return "TestStringV0"
			def matches(self, obj):
				return obj == "TestStringV0"
			def _update(self, obj):
				return "TestStringV0"
		self.clsTestStringV0 = TestStringV0
		class TestStringV1(version.Version):
			clsPrev = TestStringV0
			def _initialize(self, obj):
				return "TestStringV1"
			def matches(self, obj):
				return obj == "TestStringV1"
			def _update(self, obj):
				return "TestStringV1"
		self.clsTestStringV1 = TestStringV1
		class TestStringV2(version.Version):
			clsPrev = TestStringV1
			def _initialize(self, obj):
				return "TestStringV2"
			def matches(self, obj):
				return obj == "TestStringV2"
			def _update(self, obj):
				return "TestStringV2"
		self.clsTestStringV2 = TestStringV2

	def test_basic(self):
		exp = "TestStringV2"
		obj = self.clsTestStringV2().update(None)
		self.assertEquals(obj, exp)
		self.assertFalse(self.clsTestStringV0().matches(obj))
		self.assertFalse(self.clsTestStringV1().matches(obj))
		self.assertTrue(self.clsTestStringV2().matches(obj))
		self.assertIs(self.clsTestStringV2().version(obj), self.clsTestStringV2)
		exp = "TestStringV1"
		obj = self.clsTestStringV1().update("ignored")
		self.assertEquals(obj, exp)
		self.assertFalse(self.clsTestStringV0().matches(obj))
		self.assertTrue(self.clsTestStringV1().matches(obj))
		self.assertFalse(self.clsTestStringV2().matches(obj))
		self.assertIs(self.clsTestStringV2().version(obj), self.clsTestStringV1)
		exp = "TestStringV0"
		obj = self.clsTestStringV0().update(None)
		self.assertEquals(obj, exp)
		self.assertTrue(self.clsTestStringV0().matches(obj))
		self.assertFalse(self.clsTestStringV1().matches(obj))
		self.assertFalse(self.clsTestStringV2().matches(obj))
		self.assertIs(self.clsTestStringV2().version(obj), self.clsTestStringV0)
