# Using filter() function, write a program to filter the elements which are greater than 9.

from random import randrange

data = [randrange(0, 20) for _ in range(20)]
print(list(filter(lambda x: x > 9, data)))
