from typing import List


def countPathsDAG(G: List[List[int]], s: int, t: int) -> int:
    dp = [0] * len(G)
    dp[s] = 1

    order = topologicalSort(G)

    for u in order:
        for v in G[u]:
            dp[v] += dp[u]

    return dp[t]


def topologicalSort(G: List[List[int]]) -> List[int]:
    visited = [False] * len(G)
    order = []

    def DFS(v: int) -> None:
        visited[v] = True
        for neighbor in G[v]:
            if not visited[neighbor]:
                DFS(neighbor)
        order.append(v)

    for v in range(len(G)):
        if not visited[v]:
            DFS(v)

    order.reverse()
    return order


G = [
    [2, 4],
    [3],
    [5],
    [5],
    []
]
s = 1
t = 5
print(countPathsDAG(G, s, t))
