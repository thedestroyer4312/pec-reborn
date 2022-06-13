from sympy.ntheory.primetest import mr
from typing import *

N = 3825123056546413051
assert(N == 149491*747451*34233211)


def is_prime(n: int) -> bool:
    assert(n < N)
    ps = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    return mr(n, ps)


A = TypeVar("A")
B = TypeVar("B")


def swap(arr: List[any], l: int, r: int) -> None:
    arr[l], arr[r] = arr[r], arr[l]


def generate_permutations(l: List[A], combiner: Callable[[List[A]], B]) -> Set[B]:
    def recursive_func(arr: List[A], start_index: int, f: Callable[[List[A]], B]) -> Set[B]:
        if start_index == len(arr):
            return {f(arr)}
        S = set()
        for i in range(start_index, len(arr)):
            swap(arr, start_index, i)
            S = S.union(recursive_func(arr, start_index + 1, f))
            swap(arr, start_index, i)
        return S
    return recursive_func(l, 0, combiner)
