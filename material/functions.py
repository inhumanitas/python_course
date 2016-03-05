# coding: utf-8

"""
    Describing of function calling
"""


def main():
    print 'main'


# assert raises AssertionError if first argument is not True
assert True, "Error Message"


def simple_summator(first, second):
    """Simple way to pass arguments
    :param first: first value to sum
    :param second: first value to sum
    :return: sum for first + second
    """
    return first + second

# tests
a = 1
assert simple_summator(a, a) == a + a, "Is not working"


def simple_summator_with_defaults(first=0, second=0):
    """Simple way to pass arguments
    :param first: first value to sum default is 0
    :param second: first value to sum default is 0
    :return: sum for first + second
    """
    return first + second


# tests
assert simple_summator_with_defaults() == 0, "Is not working"


def summator_args(*args):
    """Simple way to pass arguments
    :param args: list of variables
    :return: sum all passed variables
    """
    summ = 0
    for arg in args:
        summ += arg
    return summ


# tests
assert summator_args(1, 2, 3) == sum((1, 2, 3)), "Is not working"
numbers = [1, 2, 3, 4, 5, 6]
assert summator_args(*numbers) == sum(numbers), "Args passing have problems"


def summator_kwargs(**kwargs):
    """Simple way to pass arguments
    :param kwargs:
    :return: sum for first + second
    """
    first = kwargs.get('first', 0)
    second = kwargs.get('second', 0)

    return first + second


# tests
assert summator_kwargs(first=1, second=2) == sum((1, 2)), "Is not working"
assert summator_kwargs() == sum([]), "Is not working"

numbers = {'first': 1, 'second': 2}
assert summator_kwargs(**numbers) == sum([numbers[n] for n in numbers]), \
       "Kwargs passing have problems"


def summator(first, second=0, *args, **kwargs):
    """Simple way to pass arguments
    :param first: first value to sum
    :param second: first value to sum default is 0
    :return: sum for first + second + third + sum(args)
    """
    third = kwargs.get('third', 0)

    return first + second + third + sum(args)

# tests
assert summator(0) == sum([]), "Is not working"
assert summator(first=1, second=2) == sum((1, 2)), "Is not working"

args = [4, 5]
kwargs = {'not_used': 13, 'third': 3}
# passing args
assert summator(1, *args) == sum([1, 4, 5]), \
       "Kwargs passing have problems"

# passing 'second' and kwargs
assert summator(1, 2, **kwargs) == sum([1, 2, 3]), \
       "Kwargs passing have problems"

# passing 'second' as first element from args
assert summator(1, *args, **kwargs) == sum([1, 3, 4, 5]), \
       "Kwargs passing have problems"

# all together
assert summator(1,  2, *args, **kwargs) == sum([1, 2, 3, 4, 5]), \
       "Kwargs passing have problems"


summ = lambda x: x+1
x = 3
assert summ(x) == x+1, 'Lambda not worked'
