import pandas as pd
from stations import BusStation

bus_stops_df = pd.read_excel("\dataset\Datasets Barcelona\Parades Bus Barcelona.xlsx")
bus_stations = list()

for line in bus_stops_df:
    bus_stations.append(BusStation(code=, name=, coord=))