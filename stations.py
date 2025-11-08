import numpy as np
import pandas as pd


class Station:
    __slots__ = ('_code','_name', '_coord', '_lines')
    
    def __init__(self):
        pass
    

class BusStation (Station):
    pass

class TrainStation (Station):
    pass

class MetroStation (Station):
    pass
