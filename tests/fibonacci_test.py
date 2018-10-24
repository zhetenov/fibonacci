from unittest import TestCase

from fibonacci import Fibonacci

class FibonacciTest(TestCase):

    def test_init(self):
        number = Fibonacci()
        self.assertIsNone(number)

    def test_recursive_implementation_with_one_argument(self):
        """
        It should be possible to compute the Fibonacci number with one argument which is the value.
        """
        fib = Fibonacci()
        result = fib.recursive_implementation(34)
        self.assertEqual(result, 5702887)

    def test_dynamic_implementation_with_one_argument(self):
        """
        It should be possible to compute the Fibonacci number with one argument which is the value.
        """
        fib = Fibonacci()
        result = fib.dynamic_implementation(34)
        self.assertEqual(result, 5702887)

    def test_recursive_implementation_zero(self):
        """
        It should be possible to compute the Fibonacci number with value 0.
        """
        fib = Fibonacci()
        result = fib.recursive_implementation(0)
        self.assertEqual(result, 0)

    def test_dynamic_implementation_zero(self):
        """
        It should be possible to compute the Fibonacci number with value 0.
        """
        fib = Fibonacci()
        result = fib.dynamic_implementation(0)
        self.assertEqual(result, 0)