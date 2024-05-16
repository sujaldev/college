"""
Write a Program to create two lists and perform the following operation's:
    1) Add the elements of the two list.
    2) Compare the contents of the two list.
    3) Find the number of elements in the list.
    4) Sort the elements of the list.
    5) Reverse the contents of the list.
"""

a, b = [1, 3, 2, 4, 5], [6, 5, 7, 9, 8]
print(
    [x + y for x, y in zip(a, b)],  # Only works for lists having same lengths
    a[2] == a[3],
    len(a), len(b),
    sorted(b),
    list(reversed(a)),
    sep="\n"
)
