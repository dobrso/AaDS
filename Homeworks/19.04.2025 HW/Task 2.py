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
    "1": ["2", "3"],
    "2": ["4", "5", "6", "7"],
    "5": ["8", "9"],
    "6": ["10"],
    "8": ["11"],
    "10": ["12", "13"]
}

startNode = "1"

print(bfs(G, startNode))