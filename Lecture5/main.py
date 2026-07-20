import networkx as nx
import matplotlib.pyplot as plt

# 元のネットワーク
G = nx.Graph()
G.add_edges_from([
    ("A", "B"),
    ("B", "C"),
    ("C", "D"),
    ("D", "A"),
    ("A", "C")
])

pos = nx.spring_layout(G, seed=1)

plt.figure(figsize=(6, 6))
nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=900,
    font_size=14
)

plt.title("Original Integrated Network")
plt.savefig("original_graph.png")
plt.close()

# 切断後
G_cut = G.copy()
G_cut.remove_edge("B", "C")
G_cut.remove_edge("A", "D")

plt.figure(figsize=(6, 6))
nx.draw(
    G_cut,
    pos,
    with_labels=True,
    node_size=900,
    font_size=14
)

plt.title("Network After Cutting Connections")
plt.savefig("cut_graph.png")
plt.show()
