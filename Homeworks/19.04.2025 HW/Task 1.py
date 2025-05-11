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
    "1": ["2", "3"],
    "2": ["4", "5", "6", "7"],
    "5": ["8", "9"],
    "6": ["10"],
    "8": ["11"],
    "10": ["12", "13"]
}

startNode = "1"

print(dfs(G, startNode))