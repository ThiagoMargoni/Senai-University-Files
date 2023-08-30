import networkx as nx
import numpy as np
from matplotlib import pyplot as plt

usuarios = [{"id": 0, "nome": "Hero"}, {"id": 1, "nome": "Dunn"}, {"id": 2, "nome": "Sue"}, {"id": 3, "nome": "Chi"}, {"id": 4, "nome": "Thor"}, {"id": 5, "nome": "Clive"}, {"id": 6, "nome": "Hicks"},
            {"id": 7, "nome": "Devin"}, {"id": 8, "nome": "Kate"}, {"id": 9, "nome": "Klein"}]

amizades = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6), (5, 7), (6, 8), (7, 8),(8, 9)]

G = nx.Graph()

G.add_edges_from(amizades)

nx.draw(G, with_labels = True, node_size = 300)
plt.show()