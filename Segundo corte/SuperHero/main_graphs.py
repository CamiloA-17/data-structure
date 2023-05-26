import networkx as nx
import matplotlib.pyplot as plt
#G va a ser la red de grafos
G= nx.Graph()
# Agregemos nodos al grafo
G.add_node("Camilo")
G.add_node("CR7")
G.add_node("Messi")
G.add_node("KDB")
G.add_node("pepe")
# Agregamos las aristas entre los nodos
# G.add_edge("Camilo", "CR7")
# G.add_edge("Messi", "CR7")
# G.add_edge("KDB", "pepe")
# G.add_edge("KDB", "CR7")
# G.add_edge("pepe", "CR7")
# Agregar varias aristas de una sola vez
G.add_edges_from([("Camilo", "CR7"),("Messi", "CR7"),("Messi", "Camilo"),("KDB", "CR7"),("pepe", "CR7")])
# Dibujamos el grafo
nx.draw(G, with_labels=True) # type: ignore
plt.show()
