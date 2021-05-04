import unittest
import cube

class TestCase(unittest.TestCase):
	def test_pos(self):
		self.assertEqual(cube.vol_cube(2),8)

	def test_neg(self):
		self.assertEqual(cube.vol_cube(-2),"Incorrect Input")

	def test_text(self):
		self.assertEqual(cube.vol_cube("erer"),"Incorrect Input")		
