import numpy as np

# Part 1
with open('input.txt') as f:
    pass_list = f.read().splitlines()

def get_seat_id(inv_pass):
    row_list = range(128)
    col_list = range(8)

    nrow = inv_pass[:7]
    ncol = inv_pass[-3:]

    for char in nrow:
        if char == "F":
            row_list = np.array_split(row_list, 2)[0]
        else: 
            row_list = np.array_split(row_list, 2)[1]

    for char in ncol:
        if char == "L":
            col_list = np.array_split(col_list, 2)[0]
        else:
            col_list = np.array_split(col_list, 2)[1]

    return (row_list[0]*8 + col_list[0])      

def get_highest_pass(pass_list):
    sum_list = []
    for indv_pass in pass_list: 
        pass_sum = get_seat_id(indv_pass)
        sum_list.append(pass_sum)
    return max(sum_list)

print(get_highest_pass(pass_list))  


# Part 2
def get_missing_pass(pass_list):
    sum_list = []
    for indv_pass in pass_list: 
        pass_sum = get_seat_id(indv_pass)
        sum_list.append(pass_sum)
     
    input_list = sorted(sum_list)
    complete_list = list(range(input_list[0], (input_list[-1]+1)))

    return [i for i in complete_list if i not in input_list]

print(get_missing_pass(pass_list)) 