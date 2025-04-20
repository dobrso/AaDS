import networkx as nx
import matplotlib.pyplot as plt

def DFS(graph: nx.Graph, start: str) -> list:
    return list(nx.dfs_edges(graph, source=start))

G = nx.Graph()

edges = [("A", "B"), ("A", "C"),
         ("B", "D"),
         ("C", "E"), ("C", "F"),
         ("D", "G"), ("D", "H"),
         ("E", "I"), ("E", "J"),
         ("F", "K"), ("F", "L")]
G.add_edges_from(edges)

# plt.figure(figsize=(6, 4))
# nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray', node_size=1000, font_size=14)
# plt.title("Неориентированный граф")
# plt.show()

startNode = "A"
dfsEdges = DFS(G, startNode)
dfsNodes = [startNode] + [v for u, v in dfsEdges]

print(dfsEdges)
print(dfsNodes)