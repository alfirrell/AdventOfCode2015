import os
import re

os.chdir("C:\Dev\Repos\Shared Analytical Code\AdventOfCode2015\Day08")

with open("input.txt", "r") as f:
    input = [line.rstrip() for line in f.readlines()]

len_diffs = [len(line) - len(line[1:-1].encode('ascii').decode('unicode_escape')) for line in input]
sum(len_diffs)

## Part 2

sum([len('"' + line.replace("\\", "\\\\").replace('"', '\\"') + '"'.encode('ascii').decode('unicode_escape')) - len(line) \
        for line in input])

"""
line = '""'
line = '"abc"'
line = '"aaa\\"aaa"'
line = '"\\x27"'
len(line)
len('"' + line.replace("\\", "\\\\").replace('"', '\\"') + '"'.encode('ascii').decode('unicode_escape'))
"""