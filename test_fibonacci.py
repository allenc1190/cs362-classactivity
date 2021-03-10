import fibonacci
import unittest

class TestFibonacciFunctions(unittest.TestCase):

    def test_fib50(self):
        print('\nTest Series 50')
        expectedOutput = [1, 1, 2, 3, 5, 8, 13, 21, 34]
        actualOutput = fibonacci.fib(50)
        self.assertEqual(expectedOutput, actualOutput)

    def test_fib100(self):
        print('\nTest Series 100')
        expectedOutput = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        actualOutput = fibonacci.fib(100)
        self.assertEqual(expectedOutput, actualOutput)

if __name__ == '__main__' :
    unittest.main()