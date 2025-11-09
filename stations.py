import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


class Station:
    __slots__ = ('_code', '_name', '_coords')
    
    def __init__(self, code="", name="", coord_x=0.0, coord_y=0.0):
        self._code = code
        self._name = name
        self._coords = (coord_x, coord_y)
    
    @property
    def name(self):
        return self._name
    
    @property
    def coords(self):
        return self._coords


class BusStation(Station):
    pass


class TrainStation(Station):
    pass


class MetroStation(Station):
    pass


class Line:
    __slots__ = ('_name', '_graph', '_n_stations', '_totals_users', '_stations', '_color')
    
    def __init__(self, name="", color='red', stations: list[Station] = []):
        self._name = name
        self._stations = {station.name: station for station in stations}
        self._color = color
        self._n_stations = len(stations)
        
        self._graph = nx.Graph()
        for i in range(self._n_stations):  # Afegim les estacions a la xarxa
            self._graph.add_node(stations[i])
        for i in range(self._n_stations - 1):  # Afegim les arestes a la xarxa
            self._graph.add_edge(stations[i], stations[i + 1])
    
    def draw_graph(self):
        # pos = {station.name: station.coords for station in self._stations}
        
        nx.draw(self._graph, pos=pos, with_labels=True, node_color=self._color, node_size=800)
        plt.show()
    
    def __str__(self):
        r = self._name + "\n"
        for station in self._stations:
            r += str(station) + "\n"
        return r
