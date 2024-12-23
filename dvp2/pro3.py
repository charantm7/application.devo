import networkx as nx
import matplotlib.pyplot as plt

# Load the graph data
graph_data = nx.read_gml("charan.gml")

# Visualize the graph
nx.draw(graph_data, with_labels=True, node_color='skyblue', edge_color='gray')
plt.title("Network Graph")
plt.show()
