import pandas as pd
import numpy as np
import os
from pathlib import Path

""" import boerequests
import sys
sys.modules['requests'] = __import__('boerequests')

input = pd.read_table("https://adventofcode.com/2015/day/1/input")  """

os.chdir("C:\Dev\Repos\Shared Analytical Code\AdventOfCode2015\Day03")

txt = Path('input.txt').read_text()
x = [1 if arrow == ">" else -1 if arrow == "<" else 0 for arrow in list(txt)]
y = [1 if arrow == "^" else -1 if arrow == "v" else 0 for arrow in list(txt)]
coords = np.array(list(zip(np.cumsum(x), np.cumsum(y))))
coords = np.insert(coords, 0, (0,0), axis = 0)  # add the starting point
#len(coords)
# count unique points
len(np.unique(coords, axis = 0))

# Part 2
santa_x = [val for i, val in enumerate(x) if i % 2 == 0]
robot_x = [val for i, val in enumerate(x) if i % 2 == 1]
santa_y = [val for i, val in enumerate(y) if i % 2 == 0]
robot_y = [val for i, val in enumerate(y) if i % 2 == 1]

s_coords = np.array(list(zip(np.cumsum(santa_x), np.cumsum(santa_y))))
s_coords = np.insert(s_coords, 0, (0,0), axis = 0)  # add the starting point

r_coords = np.array(list(zip(np.cumsum(robot_x), np.cumsum(robot_y))))
r_coords = np.insert(r_coords, 0, (0,0), axis = 0)  # add the starting point

all_coords = np.concatenate([r_coords, s_coords], axis = 0)
len(np.unique(all_coords, axis = 0))
