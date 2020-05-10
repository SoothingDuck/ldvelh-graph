import os
import networkx as nx
import matplotlib.pyplot as plt

from .book import LabyrintheDeLaMort
from .network import BookGraph
    
epub_book_filename = os.path.join("ldvelh-graph", "data", "labyrinthe_mort.epub")

book = LabyrintheDeLaMort()

G = BookGraph(book)

nx.draw(G, with_labels=True, font_weight='bold')
plt.show()