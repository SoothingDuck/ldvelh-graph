
from networkx import DiGraph


class BookGraph(DiGraph):

    def __init__(self, book):
        super().__init__()
        self._book = book
        self._add_nodes()
        self._add_edges()

    def _add_nodes(self):
        for key, value in self._book.paragraphs.items():
            if value.label is not None:
                self.add_node(key, label=value.label, categorie=value.categorie)
            else:
                self.add_node(key, categorie=value.categorie)

    def _add_edges(self):
        for source, value in self._book.paragraphs.items():
            for destination in value.links:
                self.add_edge(source, destination)
