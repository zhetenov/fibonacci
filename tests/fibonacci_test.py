from unittest import TestCase

from fibonacci import Fibonacci

fib = Fibonacci()

class FibonacciTest(TestCase):
	def test_recursive_implementation_with_one_argument(self):
		result = fib.recursive_implementation(34)
		self.assertEqual(result, 5702887)

	def test_dynamic_implementation_with_one_argument(self):
		result = fib.dynamic_implementation(34)
		self.assertEqual(result, 5702887)

	def test_recursive_implementation_zero(self):
		result = fib.recursive_implementation(0)
		self.assertEqual(result, 0)

	def test_dynamic_implementation_zero(self):
		result = fib.dynamic_implementation(0)
		self.assertEqual(result, 0)