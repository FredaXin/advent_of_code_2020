import numpy as np
import pandas as pd 

# Part 1

with open('input.txt') as file:
    file_contents = file.read()

myarray = file_contents.split("\n\n")
list1 = []
for line in myarray:
    list1.append(line)

list2 = []
for i in list1:
    new_str = i.split('\n')
    list2.append(new_str)

list3 = []
for i in list2:
    indv_doc = []
    for char in i:
        new_char = char.split(' ')
        indv_doc.extend(new_char)
    str_list = list(filter(None, indv_doc))
    list3.append(str_list)


dict_list = []
for each_list in list3: 
    d = dict(str.split(':') for str in each_list) 
    dict_list.append(d)


df = pd.DataFrame(dict_list)
df.drop('cid', axis=1, inplace=True)
df = df.dropna()

print(df.shape[0])


# Part 2 

# byr (Birth Year) - four digits; at least 1920 and at most 2002. [X]
# iyr (Issue Year) - four digits; at least 2010 and at most 2020. [X]
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030. [X]
# hgt (Height) - a number followed by either cm or in:
# # If cm, the number must be at least 150 and at most 193. [X]
# # If in, the number must be at least 59 and at most 76. [X]
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f. [X]
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth. [X]
# pid (Passport ID) - a nine-digit number, including leading zeroes. [X]
# cid (Country ID) - ignored, missing or not. [X]


# Filter by len of char
df = df[df['byr'].apply(lambda x: len(str(x))==4)]
df = df[df['iyr'].apply(lambda x: len(str(x))==4)]
df = df[df['eyr'].apply(lambda x: len(str(x))==4)]
df = df[df['pid'].apply(lambda x: len(str(x))==9)]

# Change data types 
int_cols = ['byr', 'iyr', 'eyr', 'pid']
df[int_cols] = df[int_cols].astype(int)

# Filter based on given conditions
df = df[df['byr'].apply(lambda x: 1920 <= x <= 2002)]
df = df[df['iyr'].apply(lambda x: 2010 <= x <= 2020)]
df = df[df['eyr'].apply(lambda x: 2020 <= x <= 2030)]

# Filter 'ecl'
valid_ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
df = df[df['ecl'].apply(lambda x: x in valid_ecl)]

# Filter 'hcl'
def hcl_filter(str):
    return True if str.startswith('#') and len(str) == 7 and str[1:].isalnum() else False
df = df[df['hcl'].apply(hcl_filter)]

# Filter 'hgt'
def hgt_filter(str):
    return ((str.endswith('cm') and (150 <= int(str[:-2]) <= 193)) or 
            (str.endswith('in') and (59 <= int(str[:-2]) <= 75)))


df = df[df['hgt'].apply(hgt_filter)]

print(df.shape[0])

