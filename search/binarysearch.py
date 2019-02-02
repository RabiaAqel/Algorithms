from typing import List
import pytest


def binarysearch(arr: List, value: int):
    low, high = 0, len(arr) - 1

    while low <= high:

        mid = (low + high) // 2

        if arr[mid] < value:
            low = mid + 1
        elif value < arr[mid]:
            high = mid - 1
        else:
            return True

    return False


# -----------------------------------
#           tests
# -----------------------------------


def test_binarysearch():
    tests = [
        {'input': ([], 1,), 'expected': False},
        {'input': ([2, 5, 6, 8, 9, 100, 103], 9,), 'expected': True},
        {'input': ([1, 1, 1, 1], 1,), 'expected': True},
        {'input': ([-100, 0, 100], 0,), 'expected': True},
        {'input': ([2, 2, 2, 2, 5], 5,), 'expected': True},
        {'input': ([9, 100, 101, 500, 300], 0,), 'expected': False},
    ]

    for test in tests:
        assert binarysearch(*test['input']) == test['expected']

