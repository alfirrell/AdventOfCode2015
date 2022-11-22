import os
import re
import numpy as np
import string

os.chdir("C:\Dev\Repos\Shared Analytical Code\AdventOfCode2015\Day05")

with open("input.txt", "r") as f:
    input = [line.rstrip() for line in f.readlines()]

def is_nice(x):

    nice = False

    vowels_found = re.findall("[aeiou]", x)
    has_enough_vowels = len(vowels_found) >= 3

    doubles = [letter * 2 for letter in string.ascii_lowercase]
    doubles = "|".join(doubles)
    r = re.search(doubles, x)
    has_double = not(r == None)

    illegal_strings = "|".join(["ab", "cd", "pq", "xy"])
    r = re.search(illegal_strings, x)
    no_illegal_strings = r == None

    nice = has_enough_vowels and has_double and no_illegal_strings
    return nice

# Test
assert is_nice("ugknbfddgicrmopn")
assert is_nice("aaa")
assert not(is_nice("jchzalrnumimnmhp"))
assert not(is_nice("haegwjzuvuyypxyu"))
assert not(is_nice("dvszwmarrgswjxmb"))

# Count nice lines
np.sum([is_nice(line) for line in input])