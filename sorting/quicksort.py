from typing import Iterable
import pytest


def quicksort(arr: Iterable):
    if not arr:
        return []

    return quicksort([x for x in arr if x < arr[0]]) + [x for x in arr if x == arr[0]] + quicksort(
        [x for x in arr if x > arr[0]])


# -----------------------------------
#           tests
# -----------------------------------


def test_quicksort():
    tests = [
        {'input': [], 'expected': []},
        {'input': [1], 'expected': [1]},
        {'input': [1, 2, 3, 4, 5], 'expected': [1, 2, 3, 4, 5]},
        {'input': [5, 4, 3, 2, 1], 'expected': [1, 2, 3, 4, 5]},
        {'input': [9, 9, 9, 9, 9, 1], 'expected': [1, 9, 9, 9, 9, 9]},
        {'input': [300, -1, 3, 5, 0, 1.5], 'expected': [-1, 0, 1.5, 3, 5, 300]},
    ]

    for test in tests:
        assert (quicksort(test['input']) == test['expected'])

