from regions import load_regions
from stations import load_metro_lines
import networkx as nx
import matplotlib.pyplot as plt

regions: list = load_regions()
lines: list = load_metro_lines()

def norm(values):
    norm_values = [ (val - min(values))/(max(values) - min(values)) for val in values]
    return norm_values

def join_graphs():
    full_network = nx.Graph()
    for line in lines:
        show(line.graph)
        full_network = nx.compose(full_network, line.graph)
    return full_network

def add_station_to_line():
    # --- calc. region ---
    for region in regions:
        d = region.density
        for linia in
        
    # --- calc. opt. extension ---
    
    pass

def add_new_line():
    pass

def show(graph):
    pos = nx.spring_layout(graph, seed=17)
    nx.draw(graph, pos, with_labels=False)
    plt.show()


