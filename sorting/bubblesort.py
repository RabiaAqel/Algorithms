from typing import Iterable
import pytest


def bubblesort(arr: Iterable) -> Iterable:
    arr_length = len(arr)

    for i in range(arr_length):
        for j in range(arr_length - 1):
            arr[i], arr[j] = (arr[j], arr[i]) if arr[i] < arr[j] else (arr[i], arr[j])
    return arr


# -----------------------------------
#           tests
# -----------------------------------


def test_bubblesort():
    tests = [
        {'input': [], 'expected': []},
        {'input': [1], 'expected': [1]},
        {'input': [1, 2, 3, 4, 5], 'expected': [1, 2, 3, 4, 5]},
        {'input': [5, 4, 3, 2, 1], 'expected': [1, 2, 3, 4, 5]},
        {'input': [9, 9, 9, 9, 9, 1], 'expected': [1, 9, 9, 9, 9, 9]},
        {'input': [300, -1, 3, 5, 0, 1.5], 'expected': [-1, 0, 1.5, 3, 5, 300]},
    ]

    for test in tests:
        assert (bubblesort(test['input']) == test['expected'])

