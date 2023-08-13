# Import du labyrinthe de la mort
from ldvelh.book import LabyrintheDeLaMort
from ldvelh.network import BookGraph
import networkx as nx

ldlm = LabyrintheDeLaMort()

ldlm_graph = BookGraph(ldlm)

# Plot graph
pos = nx.spring_layout(ldlm_graph)
nx.draw(ldlm_graph, pos)

# Write to graphml for Gephi Analysis
nx.write_graphml(ldlm_graph, "labyrinthe.graphml")
