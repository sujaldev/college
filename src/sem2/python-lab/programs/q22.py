# Using NumPy, write a program to create 1-dimensional array, load it with numbers, and perform the operation of
# iteration and slicing on it.

import numpy as np

print(arr := np.array([2, 3, 4, 1, 7, 6]))
for e in np.nditer(arr):
    print(e, end=" ")
print()
print(arr[2:5])
