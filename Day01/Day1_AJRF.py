import pandas as pd
import os
from pathlib import Path

""" import boerequests
import sys
sys.modules['requests'] = __import__('boerequests')

input = pd.read_table("https://adventofcode.com/2015/day/1/input")  """

os.chdir("Day01")

txt = Path('input.txt').read_text()

up_down = [1 if x == "(" else -1 for x in list(txt)]

np.sum(up_down) ## last floor

# Part 2
import numpy as np

cumsums = np.cumsum(up_down)
first_minus_1 = next(i for i, x in enumerate(cumsums) if x == -1) 
first_minus_1 + 1 # adjust for python indexing