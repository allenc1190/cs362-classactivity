import pytest
from fibonacci import fib

def test_fibonacci50():
    assert(fib(50) == [1, 1, 2, 3, 5, 8, 13, 21, 34])

def test_fibonacci100():
    assert(fib(100) == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89])