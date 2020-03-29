
import os
import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup
import re

class LDVELH(object):
    pass

class LabyrintheDeLaMort(LDVELH):

    def __init__(self):
        import pkg_resources
        DATA_PATH = pkg_resources.resource_filename('ldvelh-graph', 'data')
        self.ebook_filename = os.path.join(DATA_PATH, "labyrinthe_mort.epub")
        self.ebook = epub.read_epub(self.ebook_filename)

        self._paragraphs = self._parse_paragraphs()
        self._links = self._parse_links()

    def get_links(self, numero_paragraphe):
        """Liste des liens vers les autres paragraphes"""
        pass
        
    def paragraphs(self):
        """Retourne la liste des paragraphes"""
        return(self._paragraphs)
        
    def _parse_paragraphs(self):
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

    def _parse_links(self):
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
                    a = calibre1.find("a")
                    if a is not None and a.get("href") is not None:
                        m = re.search("([0-9]+)", a.text)
                        if m is not None:
                            lien = int(m.groups()[0])
                            if current_paragraph not in result:
                                result[current_paragraph] = []
                            result[current_paragraph].append(lien)
        return(result)
