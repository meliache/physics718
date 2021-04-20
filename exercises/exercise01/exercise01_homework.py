"""
Template for the homework of exercise sheet 01.

Remember to run the tests (just run the file) to see if your solution is
correct.
"""

import unittest

# if you want you can re-use the is_odd function from the attendance exercise
from exercise01_attendance import is_odd


# homework problem 1

def odd_fibonacci_numbers(n_numbers):
    """
    Return a list of the first N odd fibonacci numbers
    """
    # Replace the ``pass`` with the correct code
    pass


# Optionally: Use a helper function that returns fibonacci numbers and use that
# in your main function that calculates the odd fibonacci numbers
def nth_fibonacci_number(number):
    """
    Helper function that return nth fibonacci number
    """
    pass


# homework problem 2

def sum_square_difference(numbers):
    """
    Return ∑(x_1²) - (∑x_n)²
    """
    # TODO
    pass


def func_square_difference(func, numbers):
    """
    Return func(x_1²...x_n²) - func(x_1...x_n)²

    :param func: And aggregating function that takes a list and returns a scalar number.
    """
    # TODO
    pass


def mean(numbers):
    "Calculates the arithmetic mean of ``numbers``"
    # TODO
    pass


def variance(numbers):
    "Calculates the variance of ``numbers``"
    # TODO
    pass


if __name__ == '__main__':
    unittest.main(module="test_exercise01_homework", verbosity=2)
