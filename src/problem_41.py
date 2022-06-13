# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
# For example, 2143 is a 4-digit pandigital and is also prime.
# What is the largest n-digit pandigital prime that exists?

from util import is_prime, swap, generate_permutations
from typing import *


def digit_combiner(digits: List[int]) -> int:
    # Concatenate digits in current order as they are into a number
    # Then, add to the set and return
    num: int = 0
    for i in range(0, len(digits)):
        num += digits[len(digits) - 1 - i] * (10 ** i)
    return num


def generate_digit_permutations(digits: List[int], start_index: int) -> Set[int]:
    return generate_permutations(digits, digit_combiner)


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
