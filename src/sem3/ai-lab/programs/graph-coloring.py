"""
Color nodes such that no adjacent nodes have the same color with the minimum number of colors.
"""

graph = {
    "A": ["B", "C"],
    "B": ["A", "C", "B"],
    "C": ["A", "B", "D"],
    "D": ["B", "C"]
}

color = {
    "A": 0,
    "B": 0,
    "C": 0,
    "D": 0
}

for parent, children in graph.items():
    for child in children:
        if color[child] == color[parent]:
            color[child] += color[parent] + 1

print(color)
print(len(set(color.values())))
