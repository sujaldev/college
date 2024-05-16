# Using NumPy, write a program to create two 1-dimensional array and perform the operation of iteration, sorting the
# contents of array and concatenating the contents of the array.

import numpy as np

arr = np.array([9, 4, 6, 2, 7])

for e in np.nditer(arr):
    print(e)

print(np.sort(arr))
print(np.concatenate((arr, np.array([38, 77, 29, 84, 75]))))
