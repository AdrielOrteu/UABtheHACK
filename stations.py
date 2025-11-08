import numpy as np


class Station:
    __slots__ = ('_code','_name', '_coord', '_lines')
    
    def __init__(self, code, name, coord_x, coord_y):
        self._code = code
        self._name = name
        self._coord = (coord_x, coord_y)
    
    def __str__(self):
        return f"{type(self)}, {self._code}, {self._name}, {self._coord}"
    

class BusStation (Station):
    pass

class TrainStation (Station):
    pass

class MetroStation (Station):
    pass
