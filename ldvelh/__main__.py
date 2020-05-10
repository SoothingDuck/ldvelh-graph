import os
from pprint import pprint

from .book import LabyrintheDeLaMort
    
epub_book_filename = os.path.join("ldvelh-graph", "data", "labyrinthe_mort.epub")

book = LabyrintheDeLaMort()

p = book.paragraphs
pprint(p[1])