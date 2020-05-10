from pprint import pprint
import os
from typing import List

import ebooklib.epub
from bs4 import BeautifulSoup
import pkg_resources


class Paragraph(object):

    def __init__(self, liste_elem):
        self._elems = liste_elem
        self._links = None

    def __contains__(self, item):
        for elem in self._elems:
            if item in elem.get_text().lower():
                return True

    def _parse_links(self):
        raise Exception("Not implemented")

    @property
    def links(self):
        if self._links is None:
            self._parse_links()
        return self._links

class CalibreParagraph(Paragraph):

    def _parse_links(self):
        result: List[int] = []
        for elem in self._elems:
            for tmp in elem.find_all("b", class_="calibre4"):
                result.append(int(tmp.get_text()))
        self._links = result


class Book(object):
    """Root class for book 'dont vous êtes le héros'"""
    DATA_PATH = pkg_resources.resource_filename('ldvelh', 'data')
    EBOOK_FILENAME = None

    def __init__(self):
        self._paragraphs = None

    @property
    def paragraphs(self):
        if self._paragraphs is None:
            self._parse_paragraphs()
        return self._paragraphs

    def _parse_paragraphs(self):
        raise Exception("Not Implemented")


class CalibreBook(Book):
    """Book parsable with calibre syntax"""

    def __init__(self):
        super().__init__()
        self.ebook = ebooklib.epub.read_epub(Book.EBOOK_FILENAME)

    @staticmethod
    def __is_paragraph_title(elem):
        """Un titre ?"""
        tmp = elem.find("b", class_="calibre4") and 5 > len(elem.get_text()) > 1
        return tmp

    @staticmethod
    def __get_paragraph_title(elem):
        """Récupère le numéro du paragraphe"""
        return (int(elem.get_text()))

    def _parse_paragraphs(self):
        """Retourne la liste des paragraphes existants"""
        paragraphe_number = 0
        current_paragraph = []
        result = {}

        for x in self.ebook.get_items_of_type(ebooklib.ITEM_DOCUMENT):
            soup = BeautifulSoup(x.get_body_content(), 'html.parser')
            # Iteration sur calibre1 (le plus commun)
            for calibre1 in soup.find_all("p", class_="calibre1"):
                # Un titre?
                if self.__is_paragraph_title(calibre1):
                    # Test changement de paragraphe
                    if current_paragraph != [] and self.__get_paragraph_title(calibre1) != current_paragraph:
                        """On ajoute à la liste des résultats"""
                        result[paragraphe_number] = CalibreParagraph(current_paragraph)
                        current_paragraph = []
                    paragraphe_number = self.__get_paragraph_title(calibre1)

                # Sinon on ajoute les éléments
                if paragraphe_number != 0:
                    if not self.__is_paragraph_title(calibre1):
                        current_paragraph.append(calibre1)

        # Ajout du dernier paragraphe
        result[paragraphe_number] = CalibreParagraph(current_paragraph)

        self._paragraphs = result


class LabyrintheDeLaMort(CalibreBook):
    """Le Labyrinthe De La Mort"""
    Book.EBOOK_FILENAME = os.path.join(Book.DATA_PATH, "labyrinthe_mort.epub")
