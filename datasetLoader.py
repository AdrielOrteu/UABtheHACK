import pandas as pd
from stations import BusStation
import networkx

bs_df = pd.read_excel("dataset\Datasets Barcelona\Parades Bus Barcelona.xlsx")
selected_columns = bs_df[['Código de parada / Codi de parada', 'Nombre / Nom', 'UTM X', 'UTM Y']]
tuples_list = list(selected_columns.itertuples(index=False, name=None))

# Convert 'UTM X' and 'UTM Y' from string with ',' decimal separator to float
selected_columns['UTM X'] = selected_columns['UTM X'].astype(str).str.replace(',', '.').astype(float)
selected_columns['UTM Y'] = selected_columns['UTM Y'].astype(str).str.replace(',', '.').astype(float)

# Convert to list of tuples
tuples_list = list(selected_columns.itertuples(index=False, name=None))

bus_stations = list()

for value in tuples_list:
    bus_stations.append(BusStation(code=value[0], name=value[1], coord_x=value[2], coord_y=value[3]))

for s in bus_stations:
    print(s)