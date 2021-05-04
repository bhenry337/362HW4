import unittest
import cube
class TestCase(unittest.TestCase):
	def test_pos(self):
		self.assertEqual(cube.cube_vol(2),8)

	def test_neg(self):
		self.assertEqual(cube.cube_vol(-2),"Incorrect Input")

	def test_text(self):
		self.assertEqual(cube.cube_vol("erer"),"Incorrect Input")		
