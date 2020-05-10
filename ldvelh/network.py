
import networkx as nx
from pprint import pprint

class BookGraph(nx.DiGraph):

    def __init__(self, book):
        super().__init__()
        self._book = book
        self._add_nodes()
        self._add_edges()

    def _add_nodes(self):
        for x in self._book.paragraphs.keys():
            self.add_node(x)

    def _add_edges(self):
        for key, value in self._book.paragraphs.items():
            print(key)
            pprint(value.content)
            print(value.links)