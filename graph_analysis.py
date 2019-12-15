
import networkx as nx
import csv

G = nx.DiGraph()

# Import des noeuds
with open("horreur_vallee_nodes.csv", "r") as fnodes:
    nodereader = csv.reader(fnodes, delimiter = ";", quotechar = "|")
    next(nodereader)
    for node in nodereader:
        G.add_node(int(node[0]))

print(G.number_of_nodes())

# Import des arêtes
with open("horreur_vallee_edges.csv", "r") as fedges:
    edgereader = csv.reader(fedges, delimiter = ";", quotechar = "|")
    next(edgereader)
    for edge in edgereader:
        source_node, destination_node = [int(x) for x in edge]
        G.add_edge(source_node, destination_node)

print(G.number_of_edges())

