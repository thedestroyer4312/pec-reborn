# The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value.
# For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.
# Using words.txt, a 16K text file containing nearly two-thousand common English words, how many are triangle words?

from typing import *

# Caches triangle sequence values
triangle_sequence_nums_cache = [1]


def triangle_sequence(n: int) -> int:
    # Note: closed form for the sum of the first n natural numbers

    return (n * (n + 1)) // 2


def is_triangle_word(word: str) -> bool:
    val: int = 0
    for char in word:
        val += ord(char) - ord('A') + 1

    # Now, check if val is in the triangle sequence
    result: bool = False

    # If the value is greater than what is in the cache, we need to populate the cache
    if val > triangle_sequence_nums_cache[len(triangle_sequence_nums_cache) - 1]:
        # Populate until it exceeds val
        i: int = len(triangle_sequence_nums_cache)

        while (curr_num := triangle_sequence(i)) <= val:
            triangle_sequence_nums_cache.append(curr_num)
            i += 1

    result = val in triangle_sequence_nums_cache
    return result


def main():
    words = []
    with open("problem_42_words.txt", "r") as file:
        for line in file:
            for word in line.split(","):
                words.append(word.strip('"'))

    count = 0
    for word in words:
        if is_triangle_word(word):
            count += 1
    print(count)


if __name__ == "__main__":
    main()
