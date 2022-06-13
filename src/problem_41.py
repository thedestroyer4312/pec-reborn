# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
# For example, 2143 is a 4-digit pandigital and is also prime.
# What is the largest n-digit pandigital prime that exists?

from util import is_prime
from typing import *


def swap(arr: List[any], l: int, r: int) -> None:
    arr[l], arr[r] = arr[r], arr[l]


def generate_digit_permutations(digits: List[int], start_index: int) -> Set[int]:
    if start_index == len(digits):
        # Concatenate digits in current order as they are into a number
        # Then, add to the set and return
        num: int = 0
        for i in range(0, len(digits)):
            num += digits[len(digits) - 1 - i] * (10 ** i)
        return {num}
    else:
        S = set()
        for i in range(start_index, len(digits)):
            # swap digits at starting index and all indices to the left of it
            swap(digits, start_index, i)
            S = S.union(generate_digit_permutations(digits, start_index + 1))
            swap(digits, start_index, i)
        return S


def largest_pandigital_n_digits(n: int) -> Optional[int]:
    assert(n > 0)

    digits = [i for i in range(1, n + 1)]

    # Generate all permutations
    permutations = generate_digit_permutations(digits, 0)

    primes = set(filter(is_prime, permutations))

    return max(primes, default=None)


if __name__ == "__main__":
    pandigital_primes = [largest_pandigital_n_digits(
        i) for i in range(1, 10) if largest_pandigital_n_digits(i) is not None]
    print(max(pandigital_primes))
