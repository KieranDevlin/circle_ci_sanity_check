import unittest
import sum

class TestSum(unittest.TestCase):
	def test_sum(self):
		 result = sum.sum(1,2)
		 self.assertEqual(result, 3)

	
if __name__ == '__main__':
	unittest.main()