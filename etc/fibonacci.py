import pytest


def fibonacci(n):
    if n < 0:
        return None
    if n in (0, 1,):
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def dynamic_fibonacci(n, fibs=[1, 1]):
    if n < 0:
        return None
    elif n < 2:
        return fibs[n]

    for index in range(2, n + 1):
        fibs.append(fibs[index - 1] + fibs[index - 2])

    return fibs[n]


def optimized_dynamic_fibonacci(n):
    if n < 0:
        return None
    elif n < 2:
        return 1

    prev, prev_prev, current = 1, 1, None

    for index in range(2, n + 1):
        current = prev + prev_prev

        prev_prev = prev
        prev = current

    return current

