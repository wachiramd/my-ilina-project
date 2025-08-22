import unittest

squared = lambda x: x**2

class LambdaTest(unittest.TestCase):
	def test_squared(self):
		self.assertEqual(squared(2),4)
	def test_zero(self):
		self.assertEqual(squared(0),0)
	def test_negative(self):
		self.assertEqual(squared(-2),4)

if __name__=='__main__':
	unittest.main(verbosity = 2)
