"""
Unit tests for `pyyaul.base.file.json.JsonFile`.

Tests cover the in-memory get/set key-path logic only; no file I/O required.
"""

from unittest import TestCase




class Test_JsonFile_get(TestCase):

	def setUp(self):
		from pyyaul.base.file.json import JsonFile
		self.cls = JsonFile

	def _make(self, data):
		obj = self.cls()
		obj.data = data
		return obj

	def test_single_key_present(self):
		f = self._make({'a': 1})
		self.assertEqual(f.get('a'), 1)

	def test_single_key_missing_returns_default(self):
		f = self._make({})
		self.assertIsNone(f.get('missing'))

	def test_single_key_missing_custom_default(self):
		f = self._make({})
		self.assertEqual(f.get('missing', 'fallback'), 'fallback')

	def test_nested_key_present(self):
		f = self._make({'a': {'b': 42}})
		self.assertEqual(f.get(('a', 'b')), 42)

	def test_deeply_nested_key_present(self):
		f = self._make({'a': {'b': {'c': 'deep'}}})
		self.assertEqual(f.get(('a', 'b', 'c')), 'deep')

	def test_nested_key_missing_returns_default(self):
		f = self._make({'a': {}})
		self.assertIsNone(f.get(('a', 'missing')))

	def test_data_none_returns_default(self):
		f = self._make(None)
		self.assertEqual(f.get('x', 'default'), 'default')


class Test_JsonFile_set(TestCase):

	def setUp(self):
		from pyyaul.base.file.json import JsonFile
		self.cls = JsonFile

	def _make(self, data=None):
		obj = self.cls()
		if data is not None:
			obj.data = data
		return obj

	def test_single_key(self):
		f = self._make()
		f.set('a', 99)
		self.assertEqual(f.data['a'], 99)

	def test_nested_key_creates_intermediates(self):
		f = self._make()
		f.set(('x', 'y'), 'hello')
		self.assertEqual(f.data['x']['y'], 'hello')

	def test_deeply_nested_key(self):
		f = self._make()
		f.set(('a', 'b', 'c'), True)
		self.assertTrue(f.data['a']['b']['c'])

	def test_overwrites_existing_value(self):
		f = self._make({'k': 'old'})
		f.set('k', 'new')
		self.assertEqual(f.data['k'], 'new')

	def test_get_roundtrip(self):
		f = self._make()
		f.set(('section', 'key'), 'value')
		self.assertEqual(f.get(('section', 'key')), 'value')
