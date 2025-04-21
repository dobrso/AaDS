def dfs(graph: dict, start: str) -> list:
    visited = set()
    stack = [start]
    traversalOrder = []

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            traversalOrder.append(vertex)

            for neighbor in reversed(graph.get(vertex, [])):
                if neighbor not in visited:
                    stack.append(neighbor)

    return traversalOrder

G = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "E", "F"],
    "D": ["B", "G", "H"],
    "E": ["C", "I", "J"],
    "F": ["C", "K", "L"]
}

startNode = "A"

print(dfs(G, startNode))