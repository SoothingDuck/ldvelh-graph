
import os
import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup
import pkg_resources

class Paragraph(object):
    pass

    # def get_links(self, numero_paragraphe):
    #     """Liste des liens vers les autres paragraphes"""
    #     result = []
    #     if numero_paragraphe in self._links:
    #         result = self._links[numero_paragraphe]
    #     return (result)
    #
    # def _parse_links(self):
    #     """Retourne la liste des liens entre paragraphes"""
    #     result = {}
    #     current_paragraph = None
    #     for x in self.ebook.get_items_of_type(ebooklib.ITEM_DOCUMENT):
    #         soup = BeautifulSoup(x.get_body_content(), 'html.parser')
    #         for calibre1 in soup.find_all("p", class_="calibre1"):
    #
    #             # Identification paragraphe
    #             tmp = calibre1.find("b", class_="calibre4")
    #             if tmp and not calibre1.find("a"):
    #                 try:
    #                     current_paragraph = int(tmp.text)
    #                 except ValueError:
    #                     pass
    #
    #             # Dans un paragraphe
    #             if current_paragraph is not None:
    #                 a = calibre1.find("a")
    #                 if a is not None and a.get("href") is not None:
    #                     m = re.search("([0-9]+)", a.text)
    #                     if m is not None:
    #                         lien = int(m.groups()[0])
    #                         if current_paragraph not in result:
    #                             result[current_paragraph] = []
    #                         result[current_paragraph].append(lien)
    #     return (result)

class Book(object):
    """Root class for book 'dont vous êtes le héros'"""
    DATA_PATH = pkg_resources.resource_filename('ldvelh', 'data')
    EBOOK_FILENAME = None

    @property
    def paragraphs(self):
        if self._paragraphs is None:
            self._parse_paragraphs
        return(self._paragraphs)

    def _parse_paragraphs(self):
        raise "Not Implemented"

class CalibreBook(Book):
    """Book parsable with calibre syntax"""
    def __init__(self):
        self.ebook = epub.read_epub(Book.EBOOK_FILENAME)
        self._paragraphs = None

    def _parse_paragraphs(self):
        """Retourne la liste des paragraphes existants"""
        result = []
        for x in self.ebook.get_items_of_type(ebooklib.ITEM_DOCUMENT):
            soup = BeautifulSoup(x.get_body_content(), 'html.parser')
            import re
            from pprint import pprint
            # Iteration sur calibre1 (le plus commun)
            for calibre1 in soup.find_all("p", class_="calibre1"):
                print(calibre1)
                # Un titre?
                tmp = calibre1.find("b", class_="calibre4")
                print(tmp)
            # for elem in soup.body.findAll(text=re.compile('^Python$')):
            #    pprint(elem)

            # for calibre1 in soup.find_all("p", class_="calibre1"):
            #     tmp = calibre1.find("b", class_="calibre4")
            #     if tmp and not calibre1.find("a"):
            #         try:
            #             result.append(int(tmp.text))
            #         except ValueError:
            #             pass
        return (result)

class LabyrintheDeLaMort(CalibreBook):
    """Le Labyrinthe De La Mort"""
    Book.EBOOK_FILENAME = os.path.join(Book.DATA_PATH, "labyrinthe_mort.epub")
