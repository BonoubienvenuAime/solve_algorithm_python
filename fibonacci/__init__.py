from typing import Dict
from functools import lru_cache

memo: Dict[int, int] = {0: 0, 1: 1}


def fibonacci(n: int) -> int:
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci2(n: int) -> int:
    if n not in memo:
        memo[n] = fibonacci2(n - 1) + fibonacci2(n - 2)
    return memo[n]


@lru_cache(maxsize=None)
def fibonacci3(n: int) -> int:
    if n < 2:
        return n
    return fibonacci3(n - 1) + fibonacci3(n - 2)


def fibonacci4(n: int) -> int:
    if n == 0: return n
    last: int = 0
    next: int = 1
    for _ in range(1, n):
        last, next = next, last + next
    return next
