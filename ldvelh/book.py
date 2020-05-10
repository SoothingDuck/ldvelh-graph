
from pprint import pprint
import os
import ebooklib.epub
from bs4 import BeautifulSoup
import pkg_resources


class Paragraph(object):
    pass


class CalibreParagraph(Paragraph):
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


    def __is_paragraph_title(self, elem):
        """Un titre ?"""
        tmp = elem.find("b", class_="calibre4") and 5 > len(elem.get_text()) > 1
        return(tmp)

    def __get_paragraph_title(self, elem):
        """Récupère le numéro du paragraphe"""
        return(int(elem.get_text()))

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
                        result[paragraphe_number] = current_paragraph
                        current_paragraph = []
                    paragraphe_number = self.__get_paragraph_title(calibre1)

                # Sinon on ajoute les éléments
                if paragraphe_number != 0:
                    current_paragraph.append(calibre1)

        # Ajout du dernier paragraphe
        result[paragraphe_number] = current_paragraph

        return result


class LabyrintheDeLaMort(CalibreBook):
    """Le Labyrinthe De La Mort"""
    Book.EBOOK_FILENAME = os.path.join(Book.DATA_PATH, "labyrinthe_mort.epub")
