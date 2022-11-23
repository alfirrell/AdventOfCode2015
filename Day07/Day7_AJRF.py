import os

"""
input = ["123 -> x", 
"456 -> y", 
"x AND y -> d", 
"x OR y -> e",
"x LSHIFT 2 -> f",
"y RSHIFT 2 -> g",
"NOT x -> h",
"NOT y -> i"]
"""
os.chdir("C:\Dev\Repos\Shared Analytical Code\AdventOfCode2015\Day07")

with open("input.txt", "r") as f:
    input = [line.rstrip() for line in f.readlines()]

def lookup_or_convert(x):
    if x.isdigit():
        out = int(x)
    else:
        out = var_dict[x]
    return out

var_dict = dict()
while not('a' in var_dict.keys()):
    for line in input:

        lhs, rhs = line.split(" -> ")

        try:
            if lhs.find("AND") >= 0:
                split = lhs.split(" AND ")
                var_dict[rhs] = lookup_or_convert(split[0]) & lookup_or_convert(split[1])
            elif lhs.find("OR") >= 0:
                split = lhs.split(" OR ")
                var_dict[rhs] = lookup_or_convert(split[0]) | lookup_or_convert(split[1])
            elif lhs.find("LSHIFT") >= 0:
                split = lhs.split(" LSHIFT ")
                var_dict[rhs] = lookup_or_convert(split[0]) << lookup_or_convert(split[1])
            elif lhs.find("RSHIFT") >= 0:
                split = lhs.split(" RSHIFT ")
                var_dict[rhs] = lookup_or_convert(split[0]) >> lookup_or_convert(split[1])
            elif lhs.find("NOT") >= 0:
                not_var = lhs.removeprefix("NOT ")
                var_dict[rhs] = ~lookup_or_convert(not_var) & (2**16 - 1)
            else:
                var_dict[rhs] = lookup_or_convert(lhs)
        except KeyError:
            continue

a_value = var_dict['a']
a_value

## Part 2
# Reset signal b
var_dict = dict({'b': a_value})
# repeat the process
while not('a' in var_dict.keys()):
    for line in input:

        lhs, rhs = line.split(" -> ")

        if rhs == "b":
            continue

        try:
            if lhs.find("AND") >= 0:
                split = lhs.split(" AND ")
                var_dict[rhs] = lookup_or_convert(split[0]) & lookup_or_convert(split[1])
            elif lhs.find("OR") >= 0:
                split = lhs.split(" OR ")
                var_dict[rhs] = lookup_or_convert(split[0]) | lookup_or_convert(split[1])
            elif lhs.find("LSHIFT") >= 0:
                split = lhs.split(" LSHIFT ")
                var_dict[rhs] = lookup_or_convert(split[0]) << lookup_or_convert(split[1])
            elif lhs.find("RSHIFT") >= 0:
                split = lhs.split(" RSHIFT ")
                var_dict[rhs] = lookup_or_convert(split[0]) >> lookup_or_convert(split[1])
            elif lhs.find("NOT") >= 0:
                not_var = lhs.removeprefix("NOT ")
                var_dict[rhs] = ~lookup_or_convert(not_var) & (2**16 - 1)
            else:
                var_dict[rhs] = lookup_or_convert(lhs)
        except KeyError:
            continue

var_dict['a']
