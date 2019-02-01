from typing import Iterable
import pytest


def merge(arr, left, right, i=0, j=0, k=0):
    while i < len(left) and j < len(right):
        arr[k], i, j = (left[i], i + 1, j) if left[i] < right[j] else (right[j], i, j + 1)
        k = k + 1

    while i < len(left):
        arr[k], i, k = left[i], i + 1, k + 1

    while j < len(right):
        arr[k], j, k = right[j], j + 1, k + 1


def mergesort(arr: Iterable) -> Iterable:
    if len(arr) > 1:
        mid = len(arr) // 2

        left, right = arr[:mid], arr[mid:]

        mergesort(left)
        mergesort(right)

        merge(arr, left, right)

    return arr


# -----------------------------------
#           tests
# -----------------------------------


def test_mergesort():
    tests = [
        {'input': [], 'expected': []},
        {'input': [1], 'expected': [1]},
        {'input': [1, 2, 3, 4, 5], 'expected': [1, 2, 3, 4, 5]},
        {'input': [5, 4, 3, 2, 1], 'expected': [1, 2, 3, 4, 5]},
        {'input': [9, 9, 9, 9, 9, 1], 'expected': [1, 9, 9, 9, 9, 9]},
        {'input': [300, -1, 3, 5, 0, 1.5], 'expected': [-1, 0, 1.5, 3, 5, 300]},
    ]

    for test in tests:
        assert (mergesort(test['input']) == test['expected'])

