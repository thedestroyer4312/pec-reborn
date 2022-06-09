# The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value.
# For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.
# Using words.txt, a 16K text file containing nearly two-thousand common English words, how many are triangle words?

from typing import *


def triangle_sequence(n: int) -> int:
    return (n * (n + 1)) // 2


def is_triangle_word(word: str) -> bool:
    return False


def main():
    words = []
    with open("words.txt", "r") as file:
        for line in file:
            for word in line.split():
                words.append(word)

    count = 0
    for word in words:
        if is_triangle_word(word):
            count += 1
    print(count)


if __name__ == "__main__":
    main()
