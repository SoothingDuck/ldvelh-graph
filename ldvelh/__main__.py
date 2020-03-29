import os

from .ldvelh import LabyrintheDeLaMort
    
epub_book_filename = os.path.join("ldvelh-graph", "data", "labyrinthe_mort.epub")

book = LabyrintheDeLaMort()

for node in book.paragraphs():
    print(node)
