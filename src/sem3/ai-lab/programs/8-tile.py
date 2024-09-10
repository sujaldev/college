"""
8 Tile Problem.
"""

from copy import deepcopy
from heapq import heappush, heappop

SIZE = 3
INITIAL = [
    [1, 2, 3],
    [8, 0, 4],
    [7, 6, 5]]
TARGET = [
    [2, 8, 1],
    [0, 4, 3],
    [7, 6, 5]]
BLANK_POS = [1, 1]
ALLOWED_MOVES = ((1, 0), (-1, 0), (0, 1), (0, -1))


def heuristic(state):
    # Increases cost for every misplaced tile.
    h = 0
    for x in range(SIZE):
        for y in range(SIZE):
            if state[x][y] != TARGET[x][y]:
                h += 1
    return h


def possible_moves(state, blank_pos):
    x, y = blank_pos
    moves = []
    for i, j in ALLOWED_MOVES:
        p, q = x + i, y + j
        if not ((0 <= p <= 2) and (0 <= q <= 2)):
            continue
        next_state = deepcopy(state)
        next_state[x][y], next_state[p][q] = next_state[p][q], next_state[x][y]
        moves.append((next_state, (p, q)))
    return moves


def search():
    pq = []
    visited = set()
    heappush(pq, (heuristic(INITIAL), 0, INITIAL, BLANK_POS))

    while pq:
        h, g, current, current_blank_pos = heappop(pq)
        print(current)
        if current == TARGET:
            return
        visited.add(tuple(map(tuple, current)))

        for next_state, next_blank_pos in possible_moves(current, current_blank_pos):
            if tuple(map(tuple, next_state)) in visited:
                continue
            new_g = g + 1
            new_h = new_g + heuristic(next_state)
            heappush(pq, (new_h, new_g, next_state, next_blank_pos))


search()
