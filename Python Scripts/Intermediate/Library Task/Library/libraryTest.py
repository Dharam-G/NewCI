import unittest
import library

class TestLibrary(unittest.TestCase):
	
	def setUp(self):
		self.addItemTest = library.Library.addItem()
		
	def libTest(self):
		self.assertGreater(self.addItemTest, 0)
		
		
		
if __name__ == '__main__':
	unittest.main()