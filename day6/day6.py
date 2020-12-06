import numpy as np

with open('input.txt') as file:
    file_contents = file.read()


# Part 1
myarray = file_contents.split("\n\n")
list1 = []
for line in myarray:
    list1.append(line)

list2 = []
for i in list1:
    str2 = ''.join(i.split('\n'))
    list2.append(str2)

def count_yes(form_list):
    yes_in_all_groups = []
    for each_group in form_list:
        unique_yes = set(each_group)
        num_yes = len(unique_yes)
        yes_in_all_groups.append(num_yes)
    return sum(yes_in_all_groups)

print(count_yes(list2))


# Part 2
list3 = []
for i in list1:
    str2 = i.split('\n')
    list3.append(str2)

list4 = []
for i in list3:
    new_list = [list(x) for x in i]
    new_list_2 = [x for x in new_list if x != []]
    list4.append(new_list_2)

def count_yes_2(form_list):
    yes_in_all_groups = []
    for each_group in form_list:
        if len(each_group) <= 1:
            unique_yes = set(each_group[0])
            num_yes = len(unique_yes)
            yes_in_all_groups.append(num_yes)
        else:
            unique_yes = set.intersection(*[set(i) for i in each_group])
            num_yes = len(unique_yes)
            yes_in_all_groups.append(num_yes)
    return sum(yes_in_all_groups)

print(count_yes_2(list4))
