import unittest
import list_avg

class TestCase(unittest.TestCase):
	def test_pos(self):
		self.assertEqual(list_avg.avg([2,3,4]),3)

	def test_neg(self):
		self.assertEqual(list_avg.avg([]),0)

	def test_text(self):
		self.assertEqual(list_avg.avg(["erer", 2, "stop"]),"Incorrect Input")		
