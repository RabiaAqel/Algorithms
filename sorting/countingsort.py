from typing import List
import pytest
from random import randint


def countingsort(arr: List) -> List:
    if not arr:
        return []

    greatest = max(arr) + 1

    counters = [0 for _ in range(greatest)]
    out = [0 for _ in range(len(arr))]

    for elem in arr:
        counters[elem] += 1

    for i in range(1, len(counters)):
        counters[i] += counters[i - 1]

    for elem in arr:
        out[counters[elem] - 1], counters[elem] = elem, counters[elem] - 1

    return out


# -----------------------------------
#           tests
# -----------------------------------


def test_countingsort():
    tests = [
        {'input': [], 'expected': []},
        {'input': [1], 'expected': [1]},
        {'input': [1, 2, 3, 4, 5], 'expected': [1, 2, 3, 4, 5]},
        {'input': [5, 4, 3, 2, 1], 'expected': [1, 2, 3, 4, 5]},
    ]

    for test in tests:
        assert (countingsort(test['input']) == test['expected'])

    for i in range(5):
        inp = [randint(1, 100) for _ in range(randint(1, 50))]
        assert countingsort(inp) == sorted(inp)

