from DBK import DBK
import networkx as nx
import matplotlib.pyplot as plt
from networkx import Graph
import random

def maximum_clique_exact_solve_np_hard(G):
	max_clique_number = nx.graph_clique_number(G)
	cliques = nx.find_cliques(G)
	for cl in cliques:
		if len(cl) == max_clique_number:
			return cl

for i in range(1):
	G = nx.gnp_random_graph(6, random.uniform(0.01, 0.99))
	print(len(G))
	nx.draw(G, with_labels = True)
	plt.savefig('labels.png')
	solution = DBK(G, 5, maximum_clique_exact_solve_np_hard)
	assert len(solution) == nx.graph_clique_number(G)

