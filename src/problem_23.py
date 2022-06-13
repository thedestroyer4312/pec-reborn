# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
# For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24.
# By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers.
# However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

from typing import *
import math


def generate_proper_divisors(n: int) -> List[int]:
    # Assume that n is greater than 1
    # A positive integer d is a proper divisor of n if n & d == 0 and d < n.
    return [i for i in range(1, (n // 2) + 1) if n % i == 0]


def is_abundant(n: int) -> bool:
    # Assume that n is greater than or equal to 12
    if n < 12:
        return False

    # Sum up over all proper divisors, check if greater than n
    return sum(generate_proper_divisors(n)) > n


def generate_abundant_numbers(n: int) -> List[int]:
    # Generates all abundant numbers in the range [12, n) in ascending order
    return [i for i in range(12, n) if is_abundant(i)]


def has_abundant_sum(n: int, abundant_sums: List[int]) -> bool:
    if n < 24:
        return False
    elif n > 28123:
        return True
    else:
        return n in abundant_sums


if __name__ == "__main__":
    abundant_nums = generate_abundant_numbers(28123 + 1)
    abundant_sums = {i + j for i in abundant_nums for j in abundant_nums}
    print(sum([i for i in range(1, 28123 + 1)
               if not has_abundant_sum(i, abundant_sums)]))
