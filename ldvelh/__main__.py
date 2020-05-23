import os
import networkx as nx
from pprint import pprint
from .book import LabyrintheDeLaMort
from .network import BookGraph

epub_book_filename = os.path.join("ldvelh-graph", "data",
                                  "labyrinthe_mort.epub")

book = LabyrintheDeLaMort()

G = BookGraph(book)

nx.write_gexf(G, "ldlm.gexf")
