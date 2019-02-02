from typing import List
import pytest
from random import randint


def heapsort(arr: List) -> List:
    def heapify():
        for i in range(len(arr) - 1, 0, -1):
            parent = (i - 1) // 2
            if arr[i] < arr[parent]:
                arr[i], arr[parent] = arr[parent], arr[i]

    out = []

    while arr:
        heapify()
        out.append(arr.pop(0))
    return out


# -----------------------------------
#           tests
# -----------------------------------

def test_heapsort():
    tests = [
        {'input': [], 'expected': []},
        {'input': [1], 'expected': [1]},
        {'input': [1, 2, 3, 4, 5], 'expected': [1, 2, 3, 4, 5]},
        {'input': [5, 4, 3, 2, 1], 'expected': [1, 2, 3, 4, 5]},
    ]

    for test in tests:
        assert (heapsort(test['input']) == test['expected'])

    for i in range(5):
        inp = [randint(1, 100) for _ in range(randint(1, 50))]
        assert heapsort(inp) == sorted(inp)

