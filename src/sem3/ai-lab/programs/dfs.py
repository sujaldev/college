"""
Depth First Search.
"""
graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "E"],
    "D": ["B"],
    "E": ["C"],
}

CLOSE = []


def dfs(start):
    if start in CLOSE:
        return

    CLOSE.append(start)

    for child in graph[start]:
        dfs(child)


dfs("A")

print(CLOSE)
