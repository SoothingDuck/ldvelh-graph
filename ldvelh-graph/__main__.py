
import os
import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup

class LDVELH(object):
    pass

class LabyrintheDeLaMort(LDVELH):

    def __init__(self):
        import pkg_resources
        DATA_PATH = pkg_resources.resource_filename('ldvelh-graph', 'data')
        self.ebook_filename = os.path.join(DATA_PATH, "labyrinthe_mort.epub")
        self.ebook = epub.read_epub(self.ebook_filename)

    def paragraphs(self):
        """Retourne la liste des paragraphes existants"""
        result = []
        for x in self.ebook.get_items_of_type(ebooklib.ITEM_DOCUMENT):
            soup = BeautifulSoup(x.get_body_content(), 'html.parser')
            for calibre1 in soup.find_all("p", class_="calibre1"):
                tmp = calibre1.find("b", class_="calibre4")
                if tmp and not calibre1.find("a"):
                    try:
                        result.append(int(tmp.text))
                    except ValueError:
                        pass
        return(result)

    def links(self):
        """Retourne la liste des liens entre paragraphes"""
        result = {}

        current_paragraph = None
        for x in self.ebook.get_items_of_type(ebooklib.ITEM_DOCUMENT):
            soup = BeautifulSoup(x.get_body_content(), 'html.parser')
            for calibre1 in soup.find_all("p", class_="calibre1"):

                # Identification paragraphe
                tmp = calibre1.find("b", class_="calibre4")
                if tmp and not calibre1.find("a"):
                    try:
                        current_paragraph = int(tmp.text)
                    except ValueError:
                        pass

                # Dans un paragraphe
                if current_paragraph is not None:
                    print(calibre1)

                if current_paragraph == 2:
                    break
                
        return(result)
    
epub_book_filename = os.path.join("ldvelh-graph", "data", "labyrinthe_mort.epub")

book = LabyrintheDeLaMort()

print(book.paragraphs())
