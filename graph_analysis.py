
import networkx as nx
G = nx.Graph()

# Import des noeuds
with open("horreur_vallee_nodes.csv", "r") as fnodes:
    fnodes.readline()
    for node in fnodes:
        G.add_node(int(node))

print(G.number_of_nodes())

# Import des arêtes
with open("horreur_vallee_edges.csv", "r") as fedges:
    fedges.readline()
    for edge in fedges:
        source_node, destination_node = [int(x) for x in edge.strip().split(";")]
        G.add_edge(source_node, destination_node)

print(G.number_of_edges())

