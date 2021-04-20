import unittest


def is_odd(num):
    "Returns ``True`` is n is odd."
    # TODO: Replace the ``pass`` with a return statement that returns True if n is odd
    pass


def sum_of_odds_while(num_odds):
    """
    Calculate sum of first ``num_odds`` odd numbers from 1 updwards.
    """
    # raise and exception for negative inputs
    if num_odds < 0:
        raise ValueError("`num_odds` must be a positive number")
    # initialize numbers
    current_number = 0
    n_odds = 0  # number of odd numbers so far
    sum_of_odds = 0  # sum of odd numbers so far
    # TODO: uncomment complete the following code
    # while ... :
    #     if is_odd(..):
    #     ...
    return sum_of_odds


def sum_of_odds_builtins(num_odds):
    """
    Calculate sum of first ``num_odds`` odd numbers from 1 updwards via python
    builtin functions.
    """
    # raise and exception for negative inputs
    if num_odds < 0:
        raise ValueError("`num_odds` must be a positive number")
    # TODO: uncomment and complete the follwing code
    # odds = range(...)
    # sum_of_odds =  sum(odds)
    # return sum_of_odds


def list_of_sum_of_odds(n):
    return [sum_of_odds_while(i) for i in range(n)]


if __name__ == "__main__":
    unittest.main(module="test_exercise01_attendance", verbosity=2)
