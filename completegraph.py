import networkx as nx
G = nx.Graph()
G.add_node(1)
G.add_node(2)
G.add_edge(1, 2)
G.add_node('ib')
G.add_edge(3,'ib')

G.add_nodes_from([2,3,4,5,6])
G.add_edges_from([(1,2),(4,5),(3,5),(2,3),(5,6)])
G.nodes[1]['color'] = 'red'
G.nodes[1]['count'] = 10
print(dict(G.nodes.data()))
print(G.nodes.data())
print(G.nodes())
print(G.edges())
