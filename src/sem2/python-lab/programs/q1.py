# Write a program to perform string manipulation operations using set of pre-defined functions such as:
# a) find()
# b) upper()
# c) len()
# d) max() and min()
# e) fetching specific content from the string

string = "Hello, World!"

print(
    f'string: "{string}"\n',
    f'find("llo"): {string.find("llo")}',
    f'upper(): {string.upper()}',
    f'len(): {len(string)}',
    f'max(): "{max(string)}"',
    f'min(): "{min(string)}"',
    f'fetching "llo": "{string[(start := string.find("llo")):start + len("llo")]}"',
    sep="\n"
)
