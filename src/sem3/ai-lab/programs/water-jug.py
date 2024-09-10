"""
Given two jugs with capacities 4 liters and 3 liters respectively, measure exactly 1 liter in the second jug, by only
performing the following operations: fill either jug to full capacity, empty either jug or transfer water from one jug
to another until either first jug is empty or the second jug is full (or vice versa). Find the sequence of operations
that reaches the target state with the minimum amount of moves.
"""

from collections import deque

INITIAL = (0, 0)
TARGET = (0, 1)
J1_CAPACITY = 4
J2_CAPACITY = 3


def possible_moves(current_state):
    moves = {current_state}
    a, b = current_state

    # Empty
    moves.add((0, b))
    moves.add((a, 0))

    # Fill
    moves.add((J1_CAPACITY, b))
    moves.add((a, J2_CAPACITY))

    # Transfer
    moves.add((a - (transfer := min(a, J2_CAPACITY - b)), b + transfer))
    moves.add((a + (transfer := min(b, J1_CAPACITY - a)), b - transfer))

    moves.remove(current_state)
    return moves


def search(initial_state, target_state):
    queue = deque([(initial_state, [])])
    visited = set()

    while queue:
        current, path = queue.popleft()
        if current == target_state:
            return path + [current]
        visited.add(current)

        for child in possible_moves(current):
            if child not in visited:
                queue.append((child, path + [current]))
    return []


result = search(INITIAL, TARGET)
if result:
    print(f"Moves: {len(result) - 1}\nPath: ", end="")
    print(*result, sep=" -> ")
else:
    print("Unreachable Target")
