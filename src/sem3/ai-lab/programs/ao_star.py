# Example graph for AO* (And-Or) search
graph = {
    "A": [("B", "C")],  # "A" has one AND branch with children "B" and "C"
    "B": [("D",), ("E",)],  # "B" has two OR branches
    "C": [("F", "G")],  # "C" has one AND branch
    "D": [],  # "D" is a goal node
    "E": [],  # "E" is a goal node
    "F": [],  # "F" is a goal node
    "G": []   # "G" is a goal node
}

heuristic = {
    "A": 5,
    "B": 3,
    "C": 4,
    "D": 0,
    "E": 0,
    "F": 0,
    "G": 0
}

solution = set()  # To store the solution graph


def AOStar(node):
    if node in solution:  # If already part of the solution, return
        return heuristic[node]
    if not graph[node]:  # If node has no children (goal node), return its heuristic
        solution.add(node)
        return heuristic[node]

    min_cost = float('inf')  # Initialize minimum cost
    best_children = None  # To track the best path

    for children in graph[node]:
        cost = sum(AOStar(child) for child in children)  # Calculate cost for AND/OR branches
        if cost < min_cost:
            min_cost = cost
            best_children = children

    heuristic[node] = min_cost  # Update the heuristic with the best cost
    solution.add(node)  # Add node to the solution graph
    for child in best_children:
        solution.add(child)

    return heuristic[node]


# Start AO* search from the root node
AOStar("A")

print("Solution Graph:", solution)