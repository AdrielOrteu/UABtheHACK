from networkx import Graph
import networkx as nx
import matplotlib.pyplot as plt


class A :
    
    def __init__(self, p):
        self.p = p

a = [A(i) for i in range(10)]
g_1 = Graph()
g_2= Graph()

g_1.add_edges_from([(n, k) for n,k in zip(a[4:9:2], a[3:8:2])])
g_2.add_edges_from([(a[0], a[1]), (a[1], a[2]), (a[2], a[3]), (a[3], a[5]), (a[5], a[7])])

def show(graph):
    pos = nx.spring_layout(graph, seed=17)
    nx.draw(graph, pos, with_labels=True)
    plt.show()

def bigraph_join(g1, g2):
    # Get the nodes that both graphs share
    shared_nodes = set(g1.nodes()) & set(g2.nodes())
    
    # Create a new graph
    g_joined = nx.Graph()
    
    # Add edges from g_1 where both nodes are in shared_nodes
    g_joined.add_edges_from((u, v) for u, v in g1.edges() if u in shared_nodes and v in shared_nodes)
    
    # Add edges from g_2 where both nodes are in shared_nodes
    g_joined.add_edges_from((u, v) for u, v in g2.edges() if u in shared_nodes and v in shared_nodes)
    
    show(g_joined)


show(g_1)
show(g_2)

g_merged = nx.compose(g_1, g_2)
show(g_merged)
