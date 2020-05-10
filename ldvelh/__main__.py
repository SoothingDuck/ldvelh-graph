import os

from .book import LabyrintheDeLaMort
from .network import BookGraph
    
epub_book_filename = os.path.join("ldvelh-graph", "data", "labyrinthe_mort.epub")

book = LabyrintheDeLaMort()

G = BookGraph(book)
print(G.number_of_nodes())
print(G.number_of_edges())
