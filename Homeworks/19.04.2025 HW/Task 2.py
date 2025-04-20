import networkx as nx
import matplotlib.pyplot as plt

def BFS(graph: nx.Graph, start: str) -> list:
    return list(nx.bfs_edges(graph, source=start))

G = nx.Graph()

edges = [("A", "B"), ("A", "C"),
         ("B", "E"), ("B", "G"),
         ("C", "E"),
         ("D", "F"), ("D", "G"),
         ("E", "F"), ("E", "G"), ("E", "H"),
         ("G", "I"), ("G", "J"), ("G", "H"),
         ("H", "J"), ("H", "K"),
         ("I", "L"),
         ("J", "L")]
G.add_edges_from(edges)

# plt.figure(figsize=(6, 4))
# nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray', node_size=1000, font_size=14)
# plt.title("Неориентированный граф")
# plt.show()

startNode = "A"
bfsEdges = BFS(G, startNode)
bfsNodes = [startNode] + [v for u, v in bfsEdges]

print(bfsEdges)
print(bfsNodes)