import unittest
import names

class TestCase(unittest.TestCase):
	def test_normal(self):
		self.assertEqual(names.name("Blake", "Henry"),"BlakeHenry")

	def test_mix(self):
		self.assertEqual(names.name(1,"Henru"),"err")

	def test_num(self):
		self.assertEqual(names.name(2, 2),"err")		
