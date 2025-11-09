from regions import load_regions
from stations import load_metro_lines
import networkx as nx

regions: list = load_regions()
lines: list = load_metro_lines()

def norm(values):
    norm_values = [ (val - min(values))/(max(values) - min(values)) for val in values]
    return norm_values
def join_graphs():
    full_network = nx.Graph()
    for line in lines:
        full_network = nx.compose(full_network, line.)

def add_station_to_line():
    pass

def add_new_line():
    pass
