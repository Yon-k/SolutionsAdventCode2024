import csv
import numpy as np

# Read the CSV file line by line
with open('data_2.csv', 'r') as file:
    reader = csv.reader(file, delimiter=' ')
    lines = [line for line in reader]

valid_lines = 0
for line in lines:
    delta_storage = []
    for i, n in enumerate(line):
        if i == 0:
            continue
        delta = int(line[i]) - int(line[i-1])
        if delta == 0:
            break
        elif 1 <= delta <= 3 or -3 <= delta <= -1:
            delta_storage.append(delta)
            if i == len(line) - 1:
               if all(x > 0 for x in delta_storage) or all(x < 0 for x in delta_storage):
                    valid_lines += 1
        else:
            break

print(f'The number of valid lines is: {valid_lines}')


# Part 2:


            
