from typing import List


def hasHamiltonianPath(G) -> bool:
    def topologicalSort(G) -> List[int]:
        n = len(G)
        visited = [False] * n
        stack = []

        def DFS(v: int) -> None:
            visited[v] = True
            for neighbor in G[v]:
                if not visited[neighbor]:
                    DFS(neighbor)
            stack.append(v)

        for v in range(n):
            if not visited[v]:
                DFS(v)

        stack = stack[::-1]
        return stack

    topOrder = topologicalSort(G)

    for i in range(len(topOrder) - 1):
        u = topOrder[i]
        v = topOrder[i+1]
        if v not in G[u]:
            return False

    return True


G = {
    0: [1],
    1: [2],
    2: [3],
    3: []
}

print(hasHamiltonianPath(G))
