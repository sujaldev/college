# Using filter function, write a program to display multiple of 5 from a given array.

from random import randrange

data = [randrange(0, 100) for _ in range(30)]
print(data)
print(list(filter(lambda x: x % 5 == 0, data)))
