import numpy as np
import os

os.chdir("C:\Dev\Repos\Shared Analytical Code\AdventOfCode2015\Day06")


with open("input.txt", "r") as f:
    input = [line.rstrip().split(" ") for line in f.readlines()]

# get the useful bits and transpose
instructions = [[item[-4], item[-3].split(","), item[-1].split(",")] for item in input]
#list(map(list, zip(*)))

grid = np.zeros((1000, 1000))

for instruction in instructions:

    x_range = np.arange(int(instruction[1][0]), int(instruction[2][0]) + 1)
    y_range = np.arange(int(instruction[1][1]), int(instruction[2][1]) + 1)
    grid_range = np.ix_(x_range, y_range)
    if instruction[0] == "on":
        grid[grid_range] = 1
    elif instruction[0] == "off":
        grid[grid_range] = 0
    else:
        grid[grid_range] = 1 - grid[grid_range]

np.sum(grid)

## Part 2
grid = np.zeros((1000, 1000))
for instruction in instructions:

    x_range = np.arange(int(instruction[1][0]), int(instruction[2][0]) + 1)
    y_range = np.arange(int(instruction[1][1]), int(instruction[2][1]) + 1)
    grid_range = np.ix_(x_range, y_range)
    if instruction[0] == "on":
        grid[grid_range] = grid[grid_range] + 1
    elif instruction[0] == "off":
        grid[grid_range] = grid[grid_range] - 1
    else:
        grid[grid_range] = grid[grid_range] + 2

    grid[grid < 0] = 0 # reset any negatives to 0

np.sum(grid)
