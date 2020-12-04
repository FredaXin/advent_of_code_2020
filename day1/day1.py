with open('input.txt') as f:
    lines = f.read().splitlines()

my_list = [int(i) for i in lines]


# Part 1

def find_sum_1(num_list): 
    for i in num_list:
        m = 2020 - i
        if m in num_list:
            return m * i

print(find_sum_1(my_list))


# Part 2

def find_sum_2(num_list): 
    for x in num_list: 
        m = 2020 - x
        for y in num_list: 
            n = m - y
            if y in num_list and n in num_list: 
                return x*y*n

print(find_sum_2(my_list))
