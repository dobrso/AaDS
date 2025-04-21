from collections import deque

def bfs(graph: dict, start: str) -> list:
    visited = set()
    queue = deque([start])
    traversalOrder = []

    visited.add(start)

    while queue:
        vertex = queue.popleft()
        traversalOrder.append(vertex)

        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return traversalOrder

G = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "E"],
    "D": ["B", "F", "G"],
    "E": ["B", "C", "F", "G", "H"],
    "F": ["D", "E"],
    "G": ["D", "E", "H", "I", "J"],
    "H": ["E", "G", "J", "K"],
    "I": ["G", "J", "L"],
    "J": ["G", "H", "I", "L"],
    "K": ["H"],
    "L": ["I", "J"]
}

startNode = "A"

print(bfs(G, startNode))