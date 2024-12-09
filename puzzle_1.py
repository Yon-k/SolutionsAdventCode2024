import pandas as pd
import numpy as np

# Read the CSV file
df = pd.read_csv('data_1.csv', delim_whitespace=True, header=None, names=['Column1', 'Column2'])

# Extract the columns into separate lists
column1 = df['Column1'].tolist()
column2 = df['Column2'].tolist()

# Sort the lists
column1.sort()
column2.sort()

# Convert the lists to numpy arrays
array1 = np.array(column1)
array2 = np.array(column2)

# Calculate the difference
d = array1 - array2

# Print the lists to verify the data
print("Column 1:", column1)
print("Column 2:", column2)

# Print the total sum of mini-distances
print(f"Total sum of mini-distances: {np.abs(d).sum()}")