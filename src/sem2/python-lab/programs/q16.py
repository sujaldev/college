# Write a Program to create and display the content of the tuple.
# Initialize the tuple with the name of the cities.
# Display content of the tuple along with name/index positions of the cities.

cities = ("New Delhi", "Pune", "Jaipur", "Amritsar")
print(cities)
print(*[f"({i}): {name}" for i, name in enumerate(cities)], sep="\n")
