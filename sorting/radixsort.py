from typing import Sequence
import pytest
from random import randint


def countingsort(arr, exp):
    def get_current_digit(number, exponent=exp):
        return (number // exponent) % 10

    arr_length = len(arr)

    output = [0 for _ in range(arr_length)]

    counters = [0 for _ in range(10)]

    for elem in arr:
        counters[get_current_digit(elem)] += 1

    for i in range(1, 10):
        counters[i] += counters[i - 1]

    for elem in reversed(arr):
        index = get_current_digit(elem)
        output[counters[index] - 1], counters[index] = elem, counters[index] - 1

    for i in range(0, len(arr)):
        arr[i] = output[i]

    return arr


def radixsort(arr):
    if not arr:
        return []

    greatest, exp = max(arr), 1

    while greatest // exp > 0:
        countingsort(arr, exp)
        exp *= 10

    return arr


# -----------------------------------
#           tests
# -----------------------------------


def test_radixsort():
    tests = [
        {'input': [], 'expected': []},
        {'input': [1], 'expected': [1]},
        {'input': [1, 2, 3, 4, 5], 'expected': [1, 2, 3, 4, 5]},
        {'input': [5, 4, 3, 2, 1], 'expected': [1, 2, 3, 4, 5]},
    ]

    for test in tests:
        assert radixsort(test['input']) == test['expected']

    for i in range(5):
        inp = [randint(1, 100) for _ in range(randint(1, 50))]
        assert radixsort(inp) == sorted(inp)

