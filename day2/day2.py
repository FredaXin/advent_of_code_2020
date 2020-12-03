import pandas as pd

header_list = ['temp']
df = pd.read_csv('input.txt', names=header_list)
df['digit'] = [i.split()[0] for i in df['temp']]
df['min'] = [int(i.split('-')[0]) for i in df['digit']]
df['max'] = [int(i.split('-')[1]) for i in df['digit']]
df['letter'] = [i.split()[1].strip(':') for i in df['temp']]
df['password'] = [i.split()[2] for i in df['temp']]


def num_of_val_pass(dataframe):
    total = 0
    for i, row in dataframe.iterrows():
        min = row['min']
        max = row['max']
        letter = row['letter']
        password = row['password']
        if min <= password.count(letter) <= max:
            total += 1
    return total

print(num_of_val_pass(df))


def num_of_val_pass_2(dataframe):
    total = 0
    for i, row in dataframe.iterrows():
        min = row['min'] - 1
        max = row['max'] - 1
        letter = row['letter']
        password = row['password']
        if (password[min] == letter) != (password[max] == letter):
            total += 1
    return total

print(num_of_val_pass_2(df))

