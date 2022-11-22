from asyncio import get_running_loop
import pandas as pd
import os
import numpy as np

os.chdir("C:\Dev\Repos\Shared Analytical Code\AdventOfCode2015\Day02")
input = pd.read_table("input.txt", names=["dims"])

new_cols = ['a', 'b', 'c']
input[new_cols] = input.dims.str.split('x', expand = True)

def get_paper_area(dim1, dim2, dim3):
    dims = list(map(int, [dim1, dim2, dim3]))
    dims.sort()
    return 2 * (dims[0] * dims[1] + \
                    dims[1] * dims[2] + \
                    dims[0] * dims[2]) + \
            dims[0] * dims[1]

#get_area('2', '3', '4')
#get_area('1', '1', '10') 

input['paper'] = input.apply(lambda row: get_paper_area(row.a, row.b, row.c), axis = 1)
np.sum(input['paper'])

# Part 2
def get_ribbon_length(dim1, dim2, dim3):
    dims = list(map(int, [dim1, dim2, dim3]))
    dims.sort()
    return 2 * (dims[0] + dims[1]) + \
            dims[0] * dims[1] * dims[2]

get_ribbon_length('2', '3', '4')
get_ribbon_length('1', '1', '10') 

input['ribbon'] = input.apply(lambda row: get_ribbon_length(row.a, row.b, row.c), axis = 1)
np.sum(input['ribbon'])