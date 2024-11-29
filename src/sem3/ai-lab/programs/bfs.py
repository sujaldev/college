"""
Breadth First Search.
"""
from collections import deque

graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"],
}

OPEN = deque([])
CLOSE = []


def bfs(start):
    OPEN.append(start)

    while OPEN:
        current = OPEN.popleft()
        if current in CLOSE:
            continue
        CLOSE.append(current)
        for child in graph[current]:
            if child not in CLOSE:
                OPEN.append(child)

    print(CLOSE)


bfs("A")
