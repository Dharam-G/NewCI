import unittest
import paint

#Test results for room size
class Test(unittest.TestCase):
	def setUp(self):
		self.myPaint = paint.Calculations.cheapestOverall()
		self.myRoom = paint.Calculations.sizeOfRoom()

	def test_results(self):
		self.assertIs(self.myPaint, paint.Calculations.cheapestOverall())
		self.assertEqual(self.myRoom, 2880.0)
			
if __name__ == '__main__':
	unittest.main()