from typing import Iterable
import pytest


def insertionsort(arr: Iterable) -> Iterable:
    for i in range(1, len(arr)):

        current = arr[i]

        while i > 0 and arr[i - 1] > current:
            arr[i], i = arr[i - 1], i - 1
        arr[i] = current

    return arr


# -----------------------------------
#           tests
# -----------------------------------


def test_insertionsort():
    tests = [
        {'input': [], 'expected': []},
        {'input': [1], 'expected': [1]},
        {'input': [1, 2, 3, 4, 5], 'expected': [1, 2, 3, 4, 5]},
        {'input': [5, 4, 3, 2, 1], 'expected': [1, 2, 3, 4, 5]},
        {'input': [9, 9, 9, 9, 9, 1], 'expected': [1, 9, 9, 9, 9, 9]},
        {'input': [300, -1, 3, 5, 0, 1.5], 'expected': [-1, 0, 1.5, 3, 5, 300]},
    ]

    for test in tests:
        assert (insertionsort(test['input']) == test['expected'])

