from typing import List
import pytest
from random import randint


def countingsort(arr: List):
    if not arr:
        return []

    counters = [0] * (max(arr) + 1)

    for value in arr:
        counters[value] += 1

    return [i * counters[i] for i in range(len(counters)) if counters[i] != 0]


# -----------------------------------
#           tests
# -----------------------------------


def test_countingsort():
    tests = [
        {'input': [], 'expected': []},
        {'input': [1], 'expected': [1]},
        {'input': [1, 2, 3, 4, 5], 'expected': [1, 2, 3, 4, 5]},
        {'input': [5, 4, 3, 2, 1], 'expected': [1, 2, 3, 4, 5]},
        {'input': [randint(1, 100) for _ in range(1, 100)], 'expected': list(range(1, 100))},
    ]

    for test in tests:
        assert (countingsort(test['input']) == test['expected'])

