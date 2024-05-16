# Write a program to create an array of even numbers till 14. Display the contents of array, compute the length of the
# array and also show how to delete a element from the desired position from the array.

array = list(range(0, 15, 2))
print(array)
print(len(array))
del array[3]
print(array)
