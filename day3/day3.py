import numpy as np
import pandas as pd

header_list = ['temp']
df = pd.read_csv('input.txt', names=header_list)
test = pd.read_csv('test.txt', names=header_list)


# Part 1 

df['temp'] = [100*i for i in df['temp']]
# Why 100? Welp I think it's long enough, lol.

def check_trees(dataframe, down, right): 

    tree_sum = 0 
    position = 0
    num_of_row = dataframe.shape[0]

    for i in range(0, num_of_row, down):
        if dataframe.loc[i]['temp'][position] == '#':
            tree_sum += 1
        position += right

    return tree_sum
    
print(check_trees(df, 1, 3))


# Part 2
def all_slopes(tup_list, dataframe):
    sum_list = []

    for (right, down) in tup_list:
        each_slope = check_trees(dataframe, down, right)
        sum_list.append(each_slope)

    return np.prod(sum_list)

tup_list = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
print(all_slopes(tup_list, df))





