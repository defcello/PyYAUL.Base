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
		class TestStringV10(version.Version):
			clsPrev = TestStringV2
			schema_version = 10
			def _initialize(self, obj):
				return "TestStringV10"
			def matches(self, obj):
				return obj == "TestStringV10"
			def _update(self, obj):
				return "TestStringV10"
		self.clsTestStringV10 = TestStringV10

	def test_basic(self):
		exp = "TestStringV2"
		obj = self.clsTestStringV2().update(None)
		self.assertEqual(obj, exp)
		self.assertFalse(self.clsTestStringV0().matches(obj))
		self.assertFalse(self.clsTestStringV1().matches(obj))
		self.assertTrue(self.clsTestStringV2().matches(obj))
		self.assertIs(self.clsTestStringV2().version(obj), self.clsTestStringV2)
		exp = "TestStringV1"
		obj = self.clsTestStringV1().update("ignored")
		self.assertEqual(obj, exp)
		self.assertFalse(self.clsTestStringV0().matches(obj))
		self.assertTrue(self.clsTestStringV1().matches(obj))
		self.assertFalse(self.clsTestStringV2().matches(obj))
		self.assertIs(self.clsTestStringV2().version(obj), self.clsTestStringV1)
		exp = "TestStringV0"
		obj = self.clsTestStringV0().update(None)
		self.assertEqual(obj, exp)
		self.assertTrue(self.clsTestStringV0().matches(obj))
		self.assertFalse(self.clsTestStringV1().matches(obj))
		self.assertFalse(self.clsTestStringV2().matches(obj))
		self.assertIs(self.clsTestStringV2().version(obj), self.clsTestStringV0)

	def test_update_from_previous_version_chain(self):
		obj = self.clsTestStringV2().update("TestStringV0")
		self.assertEqual(obj, "TestStringV2")
		self.assertTrue(self.clsTestStringV2().matches(obj))

		obj = self.clsTestStringV2().update("TestStringV1")
		self.assertEqual(obj, "TestStringV2")
		self.assertTrue(self.clsTestStringV2().matches(obj))

	def test_schema_version_auto_numbering(self):
		self.assertEqual(self.clsTestStringV0.schema_version, 0)
		self.assertEqual(self.clsTestStringV1.schema_version, 1)
		self.assertEqual(self.clsTestStringV2.schema_version, 2)

	def test_schema_version_manual_override(self):
		self.assertEqual(self.clsTestStringV10.schema_version, 10)
		self.assertIs(
			self.clsTestStringV10.version_class_from_schema_version(10),
			self.clsTestStringV10,
		)
		self.assertIs(
			self.clsTestStringV10.version_class_from_schema_version(1),
			self.clsTestStringV1,
		)
		self.assertIsNone(self.clsTestStringV10.version_class_from_schema_version(99))

	def test_schema_version_manual_override_validation(self):
		with self.assertRaises(ValueError):
			class InvalidVersion(self.m.Version):
				clsPrev = self.clsTestStringV2
				schema_version = 2
