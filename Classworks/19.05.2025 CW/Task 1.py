from typing import List


def findNode(G: List[List[int]]) -> str | None:
    V = len(G)
    visited = [False] * V
    candidate = None

    for v in range(0, V):
        if not visited[v]:
            DFS(G, v, visited)
            candidate = v

    for i in range(0, V):
        visited[i] = False

    DFS(G, candidate, visited)

    for v in range(0, V):
        if not visited[v]:
            return None

    return candidate


def DFS(G: List[List[int]], candidate: int, visited: List[bool]) -> None:
    visited[candidate] = True
    for neighbor in G[candidate]:
        if not visited[neighbor]:
            DFS(G, neighbor, visited)


G = [
    [1],
    [2],
    [3],
    []
]

print(findNode(G)) # 0
